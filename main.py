from fastapi import FastAPI, HTTPException

from calculations.factorial import factorial
from calculations.fibonacci import fibonacci
from calculations.loan_repayment import loan_repayment

from typing import Annotated

from pydantic import BaseModel

app = FastAPI()


class LoanFormat(BaseModel):
    principal: float
    annual_rate: float 
    months: int


@app.post("/fibonacci/")
async def fibonacci_page(n: int):
    return fibonacci(n)


@app.post("/factorial/")
async def factorial_page(n: int):
    return factorial(n)


@app.post("/loan/")
async def loan_page(p: LoanFormat):
    try:
        result = loan_repayment(
            p.principal, 
            p.annual_rate, 
            p.months)
        
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))