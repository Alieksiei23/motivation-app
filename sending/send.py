import smtplib
from sqlalchemy import text
from fastapi import APIRouter

from settings import setting, engine, AsyncSession
from databases.scheme import Users

router = APIRouter(prefix='/send')

sender = setting.LOGIN
password = setting.EMAIL_PASSWORD



@router.post('/letter/')
async def get_all_mail():
    async with AsyncSession(engine) as conn:
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender, password)
        result = await conn.execute(text("SELECT email FROM users"))
        for email in result.scalars().all():
            server.sendmail(sender, email, 'Hello World!')
        return {
            'send': 'success'
        }
