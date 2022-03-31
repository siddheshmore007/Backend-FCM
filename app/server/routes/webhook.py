from decouple import config
import logging
import json
import razorpay

# Create and configure logger
logging.basicConfig(filename="payments.log",format='%(asctime)s %(message)s',filemode='w')

# Creating an object
logger = logging.getLogger()


client = razorpay.Client(auth=(config("RZP_TEST_KEY"), config("RZP_SECRET_KEY")))


# # Z1x2c3v4@P0o9i8u7 - sec
# client.utility.verify_webhook_signature(webhook_body, webhook_signature, webhook_secret)

# client.utility.verify_webhook_

from fastapi import Request
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder


from app.server.database import (
    
    add_payment_record,
    retrieve_payment_records,
    retrieve_payment_by_id,
    update_payment_status,
)

from app.server.models.payments import (
    PaymentRecords,
    ResponseModel,
    ErrorResponseModel,
)

webhook_router = APIRouter()

webhook_secret = config("WEBHOOK_SECRET")


@webhook_router.post('/', response_description="new payment has been captured")
async def read_webhooks(request: Request):
    try:
        raw_body = await request.body()
        head_values = request.headers
        body = jsonable_encoder(raw_body)
        json_body = json.loads(body)
        payload = json_body["payload"]
        payment_info = payload["payment_link"]
        customer = payment_info["entity"]["customer"]
        reference_id = payment_info["entity"]["reference_id"]
        link_status = payment_info["entity"]["status"]
    
        # verify = client.utility.verify_webhook_signature(body, webhook_signature, webhook_secret)
        print(head_values)

        # logger.info("New payment captured: {}".format(customer["name"]))
        # print(json_body["payload"])
        print(customer)
        print(link_status)
        print(raw_body)
    except json.JSONDecodeError:
        print("Response Content is not a valid JSON")
    finally:
        return ResponseModel(raw_body, "webhook event received")



"""
{
    "account_id":"acc_J70aiaIaz3FcjJ",
    "contains":["payment_link","order","payment"],
    "created_at":1648623852,
    "entity":"event",
    "event":"payment_link.paid",
    "payload":
    {
        "order":
        {
            "entity":
            {
                "amount":500,
                "amount_due":0,
                "amount_paid":500,
                "attempts":1,
                "created_at":1648623873,
                "currency":"INR",
                "entity":"order",
                "id":"order_JDDB1fvOfJCAAg",
                "notes":{"policy_name":"Enrollment Fees"},
                "offer_id":null,
                "receipt":null,
                "status":"paid"
            }
        },
        "payment":
        {
            "entity":
            {
                "acquirer_data":
                {
                    "rrn":"925734411313",
                    "upi_transaction_id":"D040B490CA19223892BED1D6186EF1FE"},
                    "amount":500,
                    "amount_refunded":0,
                    "amount_transferred":0,
                    "bank":null,
                    "base_amount":500,
                    "captured":true,
                    "card":null,
                    "card_id":null,
                    "contact":"+918291021910",
                    "created_at":1648623899,
                    "currency":"INR",
                    "description":"#JDDAf6zUnmCk0k",
                    "email":"morelsiddhesh25@gmail.com",
                    "entity":"payment",
                    "error_code":null,
                    "error_description":null,
                    "error_reason":null,
                    "error_source":null,
                    "error_step":null,
                    "fee":12,
                    "fee_bearer":"platform",
                    "id":"pay_JDDBUCIblAWJ8M",
                    "international":false,
                    "invoice_id":null,
                    "method":"upi",
                    "notes":{"policy_name":"Enrollment Fees"},
                    "order_id":"order_JDDB1fvOfJCAAg",
                    "refund_status":null,
                    "status":"captured",
                    "tax":2,
                    "vpa":"success@razorpay",
                    "wallet":null
                }
            },
            "payment_link":
            {
                "entity":
                {
                    "accept_partial":true,
                    "amount":500,
                    "amount_paid":500,
                    "callback_method":"get",
                    "callback_url":"https://example-callback-url.com/",
                    "cancelled_at":0,
                    "created_at":1648623852,
                    "currency":"INR",
                    "customer":
                    {
                        "contact":"8291021910",
                        "email":"morelsiddhesh25@gmail.com",
                        "name":"Siddhesh More"
                    },
                    "description":"For XYZ purpose",
                    "expire_by":0,
                    "expired_at":0,
                    "first_min_partial_amount":100,
                    "id":"plink_JDDAf6zUnmCk0k",
                    "notes":{"policy_name":"Enrollment Fees"},
                    "notify":{"email":true,"sms":true},
                    "order_id":"order_JDDB1fvOfJCAAg",
                    "reference_id":"",
                    "reminder_enable":false,
                    "reminders":{},
                    "short_url":"https://rzp.io/i/p3U6GNOKt",
                    "status":"paid",
                    "updated_at":1648623899,
                    "upi_link":false,
                    "user_id":""
                }
            }
        }
    }
}  
"""