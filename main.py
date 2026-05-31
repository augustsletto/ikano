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

class LoanResponse(BaseModel):
    monthly_repayment: str

class StandardInput(BaseModel):
    n: int
    
class FibonacciResponse(BaseModel):
    fibonacci_int: str

class FactorialResponse(BaseModel):
    factorial_int: str


@app.post("/fibonacci/", response_model=FibonacciResponse)
async def fibonacci_page(fibonacci_formatted: StandardInput):
    result = fibonacci(fibonacci_formatted.n)
    
    return FibonacciResponse(fibonacci_int=str(result))


@app.post("/factorial/", response_model=FactorialResponse)
async def factorial_page(factorial_formatted: StandardInput):
    result = factorial(factorial_formatted.n)
    return FactorialResponse(factorial_int=str(result))


@app.post("/loan/", response_model=LoanResponse)
async def loan_page(loan_formatted: LoanFormat):
    try:
        result = loan_repayment(
            loan_formatted.principal, 
            loan_formatted.annual_rate, 
            loan_formatted.months)
        
        return LoanResponse(monthly_repayment=str(result))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))