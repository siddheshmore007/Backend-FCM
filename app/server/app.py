from fastapi import FastAPI
from app.server.routes.payments import router as PaymentRouter


app = FastAPI()

app.include_router(PaymentRouter, tags=["Payment"], prefix="/payments")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}