from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder


from app.server.database import (
    
    add_payment_record,
    
)


from app.server.models.payments import (
    PaymentRecords,
    ResponseModel,
    ErrorResponseModel,
)

router = APIRouter()


@router.post("/", response_description="Payment record added into the database")
async def add_new_payment(payment_record: PaymentRecords = Body(...)):
    payment_record = jsonable_encoder(payment_record)
    new_payment_record = await add_payment_record(payment_record)
    return ResponseModel(new_payment_record, "Payment Record Added Successfully.")

