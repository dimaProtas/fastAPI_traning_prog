from fastapi import WebSocket, WebSocketDisconnect, Depends
from fastapi.routing import APIRouter
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.chat.models import Messages
from src.database import async_session_maker, get_async_session

router = APIRouter(
    prefix='/chat',
    tags=['Chat']
)



class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str, add_to_db: bool):
        if add_to_db:
            await self.add_message_to_database(message)
        for connection in self.active_connections:
            await connection.send_text(message)

    async def add_message_to_database(self, message: str):
        async with async_session_maker() as session:
            stmt = insert(Messages).values(
                message=message
            )
            await session.execute(stmt)
            await session.commit()


manager = ConnectionManager()


@router.get('/last_message')
async def get_last_message(session: AsyncSession = Depends(get_async_session)):
    query = select(Messages).order_by(Messages.id.desc()).limit(10)
    result = await session.execute(query)
    return result.scalars().all()



@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}", add_to_db=True)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat", add_to_db=False)