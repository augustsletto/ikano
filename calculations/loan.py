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
    
    # Accepts only float and int for principal and annual_rate, 
    # blocks bool specifically since it runs like 0 or 1
    # only accepts int for months input
    if isinstance (principal, bool) or not isinstance(principal, (int, float)):
        raise TypeError("n must be an integer or a float") 
    
    if isinstance (annual_rate, bool) or not isinstance(annual_rate, (int, float)):
        raise TypeError("n must be an integer or a float")
    
    if isinstance(months, bool) or not isinstance(months, int):
        raise TypeError("n must be an integer")
    
        
    # handle 0 as input value
    inputs = {"principal": principal, "annual_rate":annual_rate, "months":months}
    for key, value in inputs.items():
        if value <= 0:
            raise ValueError(f"{value} Not valid. '{key}' Must be higher than 0")
    
    P = Decimal(str(principal))
    r = Decimal(str(annual_rate)) / Decimal("12")
    n = months
    
    # loan formula
    M = P * (r*(1+r)**n / ((1+r)**n - 1))
    

    return M.quantize(Decimal("0.01"), ROUND_HALF_UP) # round up, two decimal places
    
    
    
# l = loan(0, 0.05, 48)
# print(l) # 100k, 5%, 48 months
