import math

def loan_calculation(principal, years, rate ):

    month_rate = rate/(100*12)
    preloan = (principal*month_rate*math.pow((1+month_rate), years*12))/(math.pow((1+month_rate), years*12)-1)
    total_money = preloan*years*12
    interest = total_money-principal
    print(preloan, total_money, interest)

loan_calculation(100000, 5, 6.5)