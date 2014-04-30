import urllib2
from symbols import SymbolsRetriever, CachingSymbolsRetriever, Clock


class CurrencyRates:
    def __init__(self, symbols_retriever):
        self.symbols_retriever = symbols_retriever

    def get_rate(self, from_currency, to_currency):
        symbol_to_name = self.symbols_retriever.get_symbols()
        if not (from_currency in symbol_to_name):
            raise ValueError("Invalid from currency: {}".format(from_currency))
        if not (to_currency in symbol_to_name):
            raise ValueError("Invalid to currency: {}".format(to_currency))

        url = ("http://www.gocurrency.com/v2/dorate.php?inV=1&from={}&" +
               "to={}&Calculate=Convert").format(from_currency, to_currency)
        page = urllib2.urlopen(url).read()

        start = page.rindex('<div id="converter_results"><ul><li>')
        substring = page[start:]
        start_of_payload = substring.index('<strong>') + 3
        end_of_payload = substring.index('</strong>', start_of_payload)
        interesting_stuff = substring[start_of_payload:end_of_payload]
        parts = interesting_stuff.split('=')
        value = parts[1].strip().split(' ')[0]
        return float(value)


def conversion_rate(from_currency, to_currency):
    return _currency_rates.get_rate(from_currency, to_currency)

_currency_rates = CurrencyRates(
    CachingSymbolsRetriever(SymbolsRetriever(), Clock()))
