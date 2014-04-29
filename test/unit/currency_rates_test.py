import pytest
from mock import patch, Mock
from currency_rates import CurrencyRates
from symbols import SymbolsRetriever

def test_gets_conversion_rate():
	symbols = Mock()
	symbols.get_symbols.return_value = {'abc': '', 'xyz': ''}
	with patch('currency_rates.urllib2') as urllib:
		urllib.urlopen = Mock()
		urllib.urlopen.return_value.read.return_value = (
			'<div id="converter_results"><ul><li><strong>1 x = 2 y</strong>'
		)

		assert CurrencyRates(symbols).get_rate('abc', 'xyz') == 2

def test_only_allows_valid_from_currency():
	symbols = Mock()
	symbols.get_symbols.return_value = {}
	with pytest.raises(ValueError):
		CurrencyRates(symbols).get_rate('foo', None)

def test_only_allows_valid_to_currency():
	symbols = Mock()
	symbols.get_symbols.return_value = {'foo'}
	with pytest.raises(ValueError):
		CurrencyRates(symbols).get_rate('foo', None)
