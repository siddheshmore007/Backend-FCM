from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder


from app.server.database import (
    
    add_payment_record,
    delete_payment_record,
    retrieve_payment_records,
    retrieve_payment_by_id,
    update_payment_record_data,
    update_payment_status,
    
)


from app.server.models.payments import (
    PaymentRecords,
    ResponseModel,
    ErrorResponseModel,
    UpdatePaymentRecords,
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



@router.put("/{student_id}", response_description="Update payment record")
async def update_payment_record(student_id: str, req: UpdatePaymentRecords = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_record = await update_payment_record_data(student_id, req)
    if updated_record:
        return ResponseModel(
            "Payment with ID: {} name update is successful".format(student_id),
            "Payment Record updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the payment.",
    )



@router.delete("/{student_id}", response_description="Payment record deleted from the database")
async def delete_record_by_student_id(student_id: str):
    deleted_record = await delete_payment_record(student_id)
    if deleted_record:
        return ResponseModel(
            "Payment Record with Student ID: {} removed".format(student_id), "Payment Record deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Payment record with student_id {0} doesn't exist".format(student_id)
    )