import smtplib
from email.message import EmailMessage

from celery import Celery

from src.config import GMAIL_USER, GMAIL_PASSWORD


SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465

celery = Celery('tasks', broker='redis://localhost:6379')

def get_email_template_autoteka(username: str):
    email = EmailMessage()
    email['Subject'] = 'Отчет автотеки'
    email['From'] = GMAIL_USER
    email['To'] = GMAIL_USER

    email.set_content(
        '<div>'
        f'<h1>Здравсвуйте {username}, вот ваш отчет автотеки!</h1>'
        '<img src="https://www.fonstola.ru/pic/201309/1440x900/fonstola.ru_112979.jpg" width="600px" />'
        '</div>',
        subtype='html'
    )

    return email

@celery.task
def send_email_report_autoteka(usernamr: str):
    email = get_email_template_autoteka(usernamr)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.send_message(email)


# Запуск Celery "celery -A src.tasks.tasks:celery worker --loglevel=INFO"
# Запуск Flower "celery -A src.tasks.tasks:celery flower"
