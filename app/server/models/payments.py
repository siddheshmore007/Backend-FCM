from operator import gt
from typing import Optional

from pydantic import BaseModel, Field, EmailStr, validator


class PaymentRecords(BaseModel):
    """can add regex validation for mobile number"""
    student_id: str = Field(...)
    full_name: str = Field(...)
    email: EmailStr = Field(...)
    mobile_no: str = Field(...)
    batch: str = Field(...)
    reference_id: str = Field(...)
    email_sent: bool = Field(...)
    payment_status: str = Field(...)
    

    class Config:
        schema_extra = {
            "example": {
                "student_id": "pybk01",
                "full_name": "Siddhesh More",
                "email": "moresiddhesh@gmail.com",
                "mobile_no": "1234567890",
                "batch": "Backend With Python",
                "reference_id": "pybk01",
                "email_sent": False,
                "payment_status": "Pending",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}

