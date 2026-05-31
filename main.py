from fastapi import FastAPI

from calculations.factorial import factorial
from calculations.fibonacci import fibonacci
from calculations.loan import loan


app = FastAPI()


@app.get("/fibonacci/{fibonacci_num}")
async def root(fibonacci_num):
    return {"fibonacci_num": fibonacci(fibonacci_num)}
