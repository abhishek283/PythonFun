'''
    This module demonstrates  simple tip function

'''
__author__='Abhishek Shah'

'''
    Calculate tip.
    Input Amount, percentage-> float
    Return tip amount-> float
'''
def tip_calculator(amount,perc):
    return amount*perc/100

if __name__=="__main__":
    print 'Tip Amount:',tip_calculator(25.0,12.0)