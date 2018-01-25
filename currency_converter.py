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
        cls.country_rates[country_name]={}
        cls.country_rates[country_name]['rate']=rate
        cls.country_rates[country_name]['symbol'] =symbol
        return True

    # method change country's currency rate
    @classmethod
    def change_rate(cls,country_name,rate):
        cls.country_rates[country_name]['rate'] = rate
        return True

    # method  returns country's calcualted currency amount
    def converted_amount(self,country_name,amount):
        return   True,'{}{}'.format(amount* self.country_rates[country_name]['rate'],self.country_rates[country_name]['symbol'])

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
        success= cc.add_country('India',60,'₹')
        if success:
            print 'Added India rate'
            success, india_rate_conversion = cc.converted_amount('India', 25)
            if success:
                print  india_rate_conversion
        success=cc.change_rate('India',63.37)
        if success:
            success,india_rate_conversion= cc.converted_amount('India', 25)
            if success:
                print  india_rate_conversion
        success = cc.add_country('Japan', 110.62,'¥')
        if success:
            success, japan_rate_conversion = cc.converted_amount('India', 25)
            if success:
                print  japan_rate_conversion

        success, india_rate=cc.get_currency_rate('India')
        if success:
            print india_rate
        print cc
    except Exception as  e :
        print 'Error Detail :',e

