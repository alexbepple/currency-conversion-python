from nose.tools import *

from mock import patch, Mock
from currency_rates import conversion_rate, currency_symbols

class CurrencyRates_Test:
    @istest
    def gets_conversion_rate(self):
        with patch('currency_rates.urllib2') as urllib:
            opener = Mock()
            urllib.build_opener = opener
            opener.return_value.open.return_value.read.return_value = (
                'href="/currency/foo>abc</a></td><td class="baz">foo</td>' + 
                'href="/currency/foo>xyz</a></td><td class="baz">bar</td>'
            )

            urllib.urlopen = Mock()
            urllib.urlopen.return_value.read.return_value = (
                '<div id="converter_results"><ul><li><b>1 x = 2 y</b>'
            )

            eq_(conversion_rate('abc', 'xyz'), 2)

