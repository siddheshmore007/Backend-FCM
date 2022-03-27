from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder


from app.server.database import (
    
    add_payment_record,
    retrieve_payment_records,
    retrieve_payment_by_id,
    
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



@router.get("/", response_description="Payment records retrieved Succeessfully")
async def get_all_payment_records():
    payments = await retrieve_payment_records()
    if payments:
        return ResponseModel(payments, "Payment record retrieved Successfully")
    return ResponseModel(payments, "Empty list returned")


@router.get("/{student_id}", response_description="Payment Record Retrieved")
async def get_payment_record_by_id(student_id):
    payment_record = await retrieve_payment_by_id(student_id)
    if payment_record:
        return ResponseModel(payment_record, "Payment Record Retrieved Successfully")
    return ErrorResponseModel("An Error occurred.", 404, "Payment Record for the student does not exist.")
