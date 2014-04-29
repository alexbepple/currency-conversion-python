from mock import patch, Mock
from symbols import SymbolsRetriever

def test_extracts_valid_currency_symbols():
	with patch('symbols.urllib2') as urllib:
		opener = Mock()
		urllib.build_opener = opener
		opener.return_value.open.return_value.read.return_value = (
			'href="/currency/foo>abc</a></td><td class="baz">foo</td>' + 
			'href="/currency/foo>xyz</a></td><td class="baz">bar</td>'
		)
		assert SymbolsRetriever().get_symbols() == {'abc': 'foo', 'xyz': 'bar'}

