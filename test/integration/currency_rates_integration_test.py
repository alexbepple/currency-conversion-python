from nose.tools import *
from currency_rates import conversion_rate

class CurrencyRates_Integration_Test:
    @istest
    def finds_rate_from_eur_to_usd(self):
        rate = conversion_rate('EUR', 'USD')
        assert rate > 0 and rate < 2

    @istest
    @raises(ValueError)
    def complains_about_nonexistent_from_currency(self):
        conversion_rate('foo', 'USD')
