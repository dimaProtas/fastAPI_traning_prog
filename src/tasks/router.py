from fastapi import APIRouter, Depends, BackgroundTasks

from src.auth.base_conf import current_user
from src.tasks.tasks import send_email_report_autoteka

router = APIRouter(
    prefix='/report'
)


@router.get('/autoteka')
def get_autoteka_report(user=Depends(current_user)):
    # send_email_report_autoteka.delay(user.first_name)
    return {
        'status': 200,
        'data': "Письмо отправлено",
        'detail': None,
    }


# Вариант фоновых задач с использованием BackgroundTasks из FastAPI
# @router.get('/autoteka')
# def get_autoteka_report(backgraund_tasks: BackgroundTasks, user=Depends(current_user)):
#     backgraund_tasks.add_task(send_email_report_autoteka, user.first_name)
#     return {
#         'status': 200,
#         'data': "Письмо отправлено",
#         'detail': None,
#     }