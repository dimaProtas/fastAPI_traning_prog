from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.base_conf import current_user
from src.auth.models import User
from src.cars.router import get_cars, get_cars_brand
from src.database import get_async_session

router = APIRouter(
    prefix="/index",
    tags=["Pages"]
)


templates = Jinja2Templates(directory="src/templates")


@router.get('/base')
async def index(request: Request, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    query = select(User).limit(10).offset(0)
    result = await session.execute(query)
    users = result.scalars().all()

    return templates.TemplateResponse("index.html", {"request": request, "current_user": current_user, "users": users})


@router.get("/cars/{ofset}/{limit}")
def get_cars(request: Request, cars=Depends(get_cars), user: User = Depends(current_user)):
    return templates.TemplateResponse('cars.html', {"request": request, "cars": cars, "current_user": user})


@router.get("/brand_cars/{brand_car}/{limit}")
def get_brand_cars(request: Request, cars=Depends(get_cars_brand), user: User = Depends(current_user)):
    return templates.TemplateResponse('cars.html', {"request": request, 'cars': cars, "current_user": user})


@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse('autorizen/login.html', {'request': request})

@router.get("/registration")
def registration(request: Request):
    return templates.TemplateResponse('autorizen/registration.html', {'request': request})


@router.get('/chat')
def chat(request: Request, current_user: User = Depends(current_user)):
    return templates.TemplateResponse('chat.html', {'request': request, 'current_user': current_user})


@router.get('/profile')
def profile(request: Request, current_user: User = Depends(current_user)):
    return templates.TemplateResponse('profile.html', {'request': request, 'current_user': current_user})
