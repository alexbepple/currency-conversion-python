import pytest
from mock import sentinel, call, Mock
from datetime import datetime, timedelta
from symbols import CachingSymbolsRetriever


@pytest.fixture
def another_retriever():
	another = Mock()
	another.get_symbols.return_value = sentinel.some_symbols
	return another


@pytest.fixture
def clock():
	clock = Mock()
	clock.now.return_value = datetime.now()
	return clock


@pytest.fixture
def caching_retriever(another_retriever, clock):
	return CachingSymbolsRetriever(another_retriever, clock)


def test_passes_on_the_actual_symbols(caching_retriever):
	assert caching_retriever.get_symbols() == sentinel.some_symbols
	

def test_caches_the_symbols(caching_retriever, another_retriever):
	caching_retriever.get_symbols()
	assert caching_retriever.get_symbols() == sentinel.some_symbols
	another_retriever.get_symbols.assert_called_once_with()


def test_gets_the_actual_symbols_anew_after_5_minutes(caching_retriever, another_retriever, clock):
	now = datetime.now()
	later = now + timedelta(minutes=5, seconds=1)
	clock.now.side_effect = [now, later]

	caching_retriever.get_symbols()
	caching_retriever.get_symbols()
	assert another_retriever.mock_calls == [call.get_symbols(), call.get_symbols()]

