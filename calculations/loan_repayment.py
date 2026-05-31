from decimal import Decimal, ROUND_HALF_UP
import math
def loan_repayment(principal: float, annual_rate: float, months: int) -> Decimal:
    # Accepts only float and int for principal and annual_rate, 
    # blocks bool specifically since it runs like 0 or 1
    # only accepts int for months input
    if isinstance (principal, bool) or not isinstance(principal, (int, float)):
        raise TypeError("principal must be an integer or a float") 
    
    if isinstance (annual_rate, bool) or not isinstance(annual_rate, (int, float)):
        raise TypeError("annual_rate must be an integer or a float")
    
    if isinstance(months, bool) or not isinstance(months, int):
        raise TypeError("months must be an integer")
    
    if not math.isfinite(principal):
        raise ValueError("principal must be finite")
    
    if not math.isfinite(annual_rate):
        raise ValueError("annual_rate must be finite")

    # handle 0 as input value
    if principal <= 0:
        raise ValueError("principal must be higher than 0")
    if annual_rate <= 0:
        raise ValueError("annual_rate must be higher than 0")
    if months <= 0:
        raise ValueError("months must be higher than 0")
    
    P = Decimal(str(principal))
    r = Decimal(str(annual_rate)) / Decimal("12")
    n = months
    
    # loan formula
    M = P * (r*(1+r)**n / ((1+r)**n - 1))
    

    return M.quantize(Decimal("0.01"), ROUND_HALF_UP) # round up, two decimal places

        
    
# l = loan("hej", 0.05, 48)
# print(l) # 100k, 5%, 48 months
