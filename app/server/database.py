import motor.motor_asyncio

from bson.objectid import ObjectId




# client = pymongo.MongoClient("mongodb+srv://siddhesh007:<password>@payments.pp5bw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", server_api=ServerApi('1'))
# db = client.test
# pwd=Zonex2cthreev4@trd355 
# Replace <password> with the password for the siddhesh007 user. Replace myFirstDatabase with the name of the database that connections will use by default. Ensure any option params are URL encoded.


MONGO_DETAILS = "mongodb://localhost:27017"

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


# Retrieve all the payment records  Q1w2e3r4@trading535
async def retrieve_payment_records():
    payment_records = []
    async for payments in payment_collection.find():
        payment_records.append(payment_helper(payments))
    return payment_records