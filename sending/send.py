import smtplib
import random
from email.mime.text import MIMEText
from sqlalchemy import text
from fastapi import APIRouter

from settings import setting, engine, AsyncSession

router = APIRouter(prefix='/send', tags=['отправка письма'])

sender = setting.LOGIN
password = setting.EMAIL_PASSWORD


@router.post('/letter/')
async def send_all_mail():
    async with AsyncSession(engine) as conn:
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender, password)
        users_email = await conn.execute(text("SELECT email FROM users"))
        letters = await conn.execute(text("SELECT letter FROM letters"))
        result = letters.scalars().all()
        print(result)
        for email in users_email.scalars().all():
            letter = MIMEText(random.choice(result)).as_string()
            server.sendmail(sender, email, letter)
        return {
            'send': 'success'
        }
