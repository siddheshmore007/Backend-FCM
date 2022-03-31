import motor.motor_asyncio

from bson.objectid import ObjectId
from decouple import config



# client = pymongo.MongoClient("mongodb+srv://siddhesh007:<password>@payments.pp5bw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", server_api=ServerApi('1'))
# db = client.test
# pwd=Zonex2cthreev4@trd355 
# Replace <password> with the password for the siddhesh007 user. Replace myFirstDatabase with the name of the database that connections will use by default. Ensure any option params are URL encoded.


MONGO_DETAILS = config("MONGO_URL")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.payments

payment_collection = database.get_collection("payments_collection")



# helper
def payment_helper(payment_record) -> dict:
    return {
        "id": str(payment_record["_id"]),
        "student_id": payment_record["student_id"],
        "full_name": payment_record["full_name"],
        "email": payment_record["email"],
        "mobile_no": payment_record["mobile_no"],
        "batch": payment_record["batch"],
        "reference_id": payment_record["reference_id"],
        "email_sent": payment_record["email_sent"],
        "payment_status": payment_record["payment_status"],
    }



# Create a new payment record
async def add_payment_record(payment: dict) -> dict:
    payment_record = await payment_collection.insert_one(payment)
    new_payment = await payment_collection.find_one({"_id": payment_record.inserted_id})
    return payment_helper(new_payment)


# Retrieve all the payment records
async def retrieve_payment_records():
    payment_records = []
    async for payments in payment_collection.find():
        payment_records.append(payment_helper(payments))
    return payment_records


# Retrieve payment record by id
async def retrieve_payment_by_id(student_id:str) -> dict:
    payment_record = await payment_collection.find_one({"student_id": student_id})
    if payment_record:
        return payment_helper(payment_record)



# update payment_status from pending to successful 
async def update_payment_status():
    pass
        

# update a record by id
# Update a student with a matching ID
async def update_payment_record_data(student_id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    payment_record = await payment_collection.find_one({"student_id": student_id})
    if payment_record:
        updated_paymenr_record = await payment_collection.update_one(
            {"student_id": student_id}, {"$set": data}
        )
        if updated_paymenr_record:
            return True
        return False

# delete a record
