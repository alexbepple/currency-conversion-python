from nose.tools import *

from mock import patch, Mock
from symbols import SymbolsRetriever, CachingSymbolsRetriever

class SymbolsRetriever_Test:
    @istest
    def extracts_valid_currency_symbols(self):
        with patch('symbols.urllib2') as urllib:
            opener = Mock()
            urllib.build_opener = opener
            opener.return_value.open.return_value.read.return_value = (
                'href="/currency/foo>abc</a></td><td class="baz">foo</td>' + 
                'href="/currency/foo>xyz</a></td><td class="baz">bar</td>'
            )
            eq_(SymbolsRetriever().get_symbols(), 
                    {'abc': 'foo', 'xyz': 'bar'})

from mock import sentinel, call
from datetime import datetime, timedelta

class CachingSymbolsRetriever_Test:
    def setUp(self):
        self.actual = Mock()
        self.actual.get_symbols.return_value = sentinel.some_symbols

        self.clock = Mock()
        self.clock.now.return_value = datetime.now()

        self.retriever = CachingSymbolsRetriever(self.actual, self.clock)

    @istest
    def passes_on_the_actual_symbols(self):
        eq_(self.retriever.get_symbols(), 
                sentinel.some_symbols)
        
    @istest
    def caches_the_symbols(self):
        self.retriever.get_symbols()
        eq_(self.retriever.get_symbols(), sentinel.some_symbols)
        self.actual.get_symbols.assert_called_once_with()

    @istest
    def gets_the_actual_symbols_anew_after_5_minutes(self):
        now = datetime.now()
        later = now + timedelta(minutes=5, seconds=1)
        returns = [now, now, later, later]
        def tick_time(*args):
            return returns.pop(0)

        self.clock.now.side_effect = tick_time

        self.retriever.get_symbols()
        self.retriever.get_symbols()
        eq_(self.actual.mock_calls, 
            [call.get_symbols(), call.get_symbols()])

