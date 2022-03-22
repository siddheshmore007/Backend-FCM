from typing import Optional

from pydantic import BaseModel, Field, EmailStr, validator


class PaymentRecords(BaseModel):
    student_id: str = Field(...)
    full_name: str = Field(...)
    email: EmailStr = Field(...)
    

    class Config:
        schema_extra = {
            "example": {
                "student_id": "pybk01",
                "full_name": "Siddhesh More",
                "email": "moresiddhesh@gmail.com",
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

