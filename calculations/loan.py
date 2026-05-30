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

def loan(principal: float, annual_rate: float, months: int) -> float:
    P = round(principal, 2)
    r = annual_rate / 12
    n = months
    
    # loan formula
    M = P * (r*(1+r)**n / ((1+r)**n - 1))
    
    

    return round(M, 2)
    
print(loan(100_000, 0.05, 48)) # 100k, 5%, 48 months