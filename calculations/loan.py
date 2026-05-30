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
    
    if isinstance(principal, (int, float)) and isinstance(annual_rate, (int, float)) and isinstance(months, int):
        
        
        
        # handle 0 as input value
        inputs = {"principal": principal, "annual_rate":annual_rate, "months":months}
        for key, value in inputs.items():
            if value <= 0:
                return f"{value} Not valid. '{key}' Must be higher than "
        
        P = Decimal(str(principal))
        r = Decimal(str(annual_rate)) / Decimal("12")
        n = months
        
        # loan formula
        M = P * (r*(1+r)**n / ((1+r)**n - 1))
        

        return M.quantize(Decimal("0.01"), ROUND_HALF_UP) # round up, two decimal places
    return {
        "type(principal) should be int or float": type(principal),
        "type(annual_rate) should be int or float": type(annual_rate),
        "type(months) should be int": type(months),
    }
    
    
l = loan(100000.0, 0.05, 48.1)
print(l) # 100k, 5%, 48 months
