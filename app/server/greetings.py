from decouple import config
from fastapi import (
    FastAPI, 
    BackgroundTasks, 
    Form, 
    Query,
    Body,
    Depends
)

from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from pydantic import EmailStr, BaseModel
from typing import List

class EmailSchema(BaseModel):
    email: List[EmailStr]



conf = ConnectionConfig(
    MAIL_USERNAME = config("EMAIL_ADDRESS"),
    MAIL_PASSWORD = config("EMAIL_PWD"),
    MAIL_FROM = config("EMAIL_ADDRESS"),
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="Fynd Academy",
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)




async def send_mail_in_background(
    background_tasks: BackgroundTasks,
    email_to: str
    ):

    message = MessageSchema(
        subject="Welcome to Fynd Academy",
        recipients=[email_to],
        body="Welcome to Fynd Academy",
        )

    fm = FastMail(conf)

    background_tasks.add_task(fm.send_message,message)


