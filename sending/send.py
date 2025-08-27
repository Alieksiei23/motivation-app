import smtplib
import random
from email.mime.text import MIMEText
from sqlalchemy import text
from fastapi import APIRouter, BackgroundTasks

from settings import setting, engine, AsyncSession

router = APIRouter(prefix='/send', tags=['отправка письма'])

sender = setting.LOGIN
password = setting.EMAIL_PASSWORD


def sending_letter(user_emails: list, letters: list) -> None:
    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()
    server.login(sender, password)
    for email in user_emails:
        letter = MIMEText(random.choice(letters)).as_string()
        server.sendmail(sender, email, letter)


@router.post('/letter/')
async def sending_to_all_email(bg_task: BackgroundTasks):
    async with AsyncSession(engine) as conn:
        users_email = await conn.execute(text("SELECT email FROM users"))
        letters = await conn.execute(text("SELECT letter FROM letters"))
        result = letters.scalars().all()
        bg_task.add_task(sending_letter, users_email, result)
        return {
            'send': 'success'
        }
