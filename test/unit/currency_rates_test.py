from nose.tools import *

from mock import patch, Mock
from currency_rates import CurrencyRates
from symbols import SymbolsRetriever

class CurrencyRates_Test:
    @istest
    def gets_conversion_rate(self):
        symbols = Mock()
        symbols.get_symbols.return_value = {'abc': '', 'xyz': ''}
        with patch('currency_rates.urllib2') as urllib:
            urllib.urlopen = Mock()
            urllib.urlopen.return_value.read.return_value = (
                '<div id="converter_results"><ul><li><b>1 x = 2 y</b>'
            )

            eq_(CurrencyRates(symbols).get_rate('abc', 'xyz'), 2)

    @istest
    @raises(ValueError)
    def only_allows_valid_from_currency(self):
        symbols = Mock()
        symbols.get_symbols.return_value = {}
        CurrencyRates(symbols).get_rate('foo', None)

    @istest
    @raises(ValueError)
    def only_allows_valid_to_currency(self):
        symbols = Mock()
        symbols.get_symbols.return_value = {'foo'}
        CurrencyRates(symbols).get_rate('foo', None)
