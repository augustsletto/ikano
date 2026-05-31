from fastapi import FastAPI

from calculations.factorial import factorial
from calculations.fibonacci import fibonacci
from calculations.loan import loan


app = FastAPI()


@app.get("/")
async def root():
    return loan(100_000, 0.05, 48)