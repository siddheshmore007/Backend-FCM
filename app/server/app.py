from fastapi import FastAPI, HTTPException
from app.server.routes.payments import router as PaymentRouter
from fastapi.middleware.cors import CORSMiddleware
from app.server.routes.webhook import webhook_router as StatusRouter




app = FastAPI()


# app.include_router(PaymentRouter, tags=["Payments"], prefix="/payments")


origins = [
    "http://localhost:3000/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(PaymentRouter, tags=["Payments"], prefix="/payments")

app.include_router(StatusRouter, tags=["Payment Status"], prefix="/status")



@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}