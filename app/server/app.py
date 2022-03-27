from fastapi import FastAPI, HTTPException
from app.server.routes.payments import router as PaymentRouter
from fastapi.middleware.cors import CORSMiddleware



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


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}