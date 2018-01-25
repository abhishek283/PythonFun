'''
    This module demonstrates  simple Discount Calcultor function
    It will also illustrate that if you see 50%+20% discount, than it is not 70% discount
'''
__author__='Abhishek Shah'
'''
    Calculate single discount.
    Input Amount, percentage-> float
    Return Amount after discount-> float
'''
def discount_calculator(amount,perc):
    return amount-amount*perc/100

'''
    Calculate multiple discounts.
    Input Amount, *perc_rates -> float
    Return Amount after discount-> float
'''
def multi_discount_calculator(amount,*perc_rates):
    for perc_rate in perc_rates:
        amount-=amount*perc_rate/100
    return amount

if __name__=="__main__":
    print 'Discounted Amount:',discount_calculator(amount=125.00,perc=70.0)
    print 'Discounted Amount:', multi_discount_calculator(125.00,50.0, 20.0 )