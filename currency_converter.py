import traceback
# -*- coding: utf-8 -*-
'''
This module demonstrates currency convertsion.
It is adding other country's rate compare to USD and calculates currency.
I have also added different unit tests for this.
'''
class CurrencyConverter():
    #dictionary stores all currency rates: {country name:{rate, symbol}}
    country_rates={}

    #method add new country's currency rate
    @classmethod
    def add_country(cls,country_name,rate,symbol):
        if cls.country_rates.get(country_name):
            return False,'Country Rate already defined'
        else:
            cls.country_rates[country_name]={}
            if not isinstance(rate,(int,float)):
                return False,'Invalid Rate Amount'
            cls.country_rates[country_name]['rate']=rate
            cls.country_rates[country_name]['symbol'] =symbol
            return True,'Country Rate Added Successfully'

    # method change country's currency rate
    @classmethod
    def change_rate(cls,country_name,rate):

        if cls.country_rates.get(country_name):
            if not isinstance(rate,(int,float)):
                return False, 'Invalid Rate Amount'
            cls.country_rates[country_name]['rate'] = rate
            return True,'Country Rate Changed Successfully'
        else:
            return False,'Please add Country currency rate first'

    # method  returns country's calcualted currency amount
    @classmethod
    def converted_amount(cls,country_name,amount):
        if cls.country_rates.get(country_name):
            if  isinstance(amount,(int, float)):
                return   True,'{}{}'.format(amount* cls.country_rates[country_name]['rate'],cls.country_rates[country_name]['symbol'])
            else:
                return False, 'Invalid Amount'
        else:
            return False,'Please Country define currency rate first'

    # method  returns country's currency rate
    @classmethod
    def get_currency_rate(cls,country_name):
        return  True,'{}{}'.format(cls.country_rates[country_name]['rate'],cls.country_rates[country_name]['symbol'])

    def __str__(cls):
        l=['Country currency rates: ']
        for k,v in cls.country_rates.iteritems():
           l.append('1 USD : {}{}'.format(v['rate'],v['symbol']))
        return '\n'.join(l)

if  __name__=="__main__":
    try:
        cc= CurrencyConverter()
        success,message= cc.add_country('India',60,'₹')

        if success:
            print message
            success, india_rate_conversion = cc.converted_amount('India', 25)
            if success:
                print  india_rate_conversion
        else:
            print message
            print message
        success,message=cc.change_rate('India',63.37)
        if success:
            success,india_rate_conversion= cc.converted_amount('India', 25)
            if success:
                print  india_rate_conversion
        else:
            print message
        success,message = cc.add_country('Japan', 110.62,'¥')
        if success:
            success, japan_rate_conversion = cc.converted_amount('India', 25)
            if success:
                print  japan_rate_conversion
        else:
            print message

        success, india_rate=cc.get_currency_rate('India')
        if success:
            print india_rate
        print cc
    except Exception as  e :
        print 'Error Detail :',e

