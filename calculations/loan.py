"""
Loan formula
M = P x [ r(1+r)^n / ((1+r)^n - 1) ]
P = principal, r = monthly interest rate, n = number of months, M = monthly repayment.

3 Loan repayment
Inputs: principal, annual rate, months
Output: monthly repayment
Use decimal-safe handling.
Handle zero-interest loans.
Round money clearly.
"""
from decimal import Decimal, ROUND_HALF_UP

def loan(principal: float, annual_rate: float, months: int) -> float:
    try:
        float(principal)
        float(annual_rate)
        int(months)
    except ValueError:
        return "invalid input"
    
    if annual_rate == 0:
        return "Zero interest is not allowed."
    
    P = Decimal(str(principal))
    r = Decimal(str(annual_rate)) / Decimal("12")
    n = months
    
    # loan formula
    M = P * (r*(1+r)**n / ((1+r)**n - 1))
    

    return M.quantize(Decimal("0.01"), ROUND_HALF_UP) # round up, two decimal places
    
    
    
l = loan(100_000, 0.05, 48)
print("monthly payment: ", l) # 100k, 5%, 48 months
