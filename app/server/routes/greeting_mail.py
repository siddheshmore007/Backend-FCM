from asyncio import shield
from decouple import config

import json
from pydantic import EmailStr
import razorpay


client = razorpay.Client(auth=(config("RZP_TEST_KEY"), config("RZP_SECRET_KEY")))



# client.utility.verify_webhook_signature(webhook_body, webhook_signature, webhook_secret)

# client.utility.verify_webhook_

from fastapi import BackgroundTasks, Request
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder



from app.server.models.payments import (
    PaymentRecords,
    ResponseModel,
    ErrorResponseModel,
)

from app.server.greetings import send_mail_in_background


mailhook_router = APIRouter()

webhook_secret = config("WEBHOOK_SECRET")


@mailhook_router.post('/', response_description="Greeting mail generated.")
async def generate_greeting_mail(background_tasks: BackgroundTasks, request: Request):
    try:
        raw = await request.body()
        head_values = request.headers
        body = jsonable_encoder(raw)
        json_body = json.loads(body)
        payload = json_body["payload"]
        payment_info = payload["payment_link"]
        student = payment_info["entity"]["customer"]
        student_email = student["email"]
        link_status = payment_info["entity"]["status"]
        if link_status == "paid":
            greetings = await send_mail_in_background(background_tasks, student_email)
    except json.JSONDecodeError:
        print("Response Content is not a valid JSON")
    finally:
        return ResponseModel(raw, "Greeting mail successfully sent")