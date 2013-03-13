import urllib2, re
from datetime import datetime

class CurrencyRates:
    def __init__(self):
        self.cached_symbols = None
        self.last_updated = datetime.min


    def currency_symbols(self):
        delta = datetime.now() - self.last_updated
        if (self.cached_symbols is not None) and delta.seconds <= 300:
            return self.cached_symbols

        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        url = "http://www.xe.com/iso4217.php" 
        page = opener.open(url).read()

        symbols = {}
        currency_regex = r'href="/currency/[^>]+>(...)</a></td><td class="[^"]+">([A-Za-z ]+)'
        for m in re.finditer(currency_regex, page):
            symbols[m.group(1)] = m.group(2)

        self.cached_symbols = symbols
        self.last_updated = datetime.now()
        return symbols


    def get_rate(self,from_currency, to_currency):
        symbol_to_name = currency_symbols()
        if not (from_currency in symbol_to_name):
            raise ValueError("Invalid from currency: {}".format(from_currency))
        if not (to_currency in symbol_to_name):
            raise ValueError("Invalid to currency: {}".format(to_currency))

        url = ("http://www.gocurrency.com/v2/dorate.php?inV=1&from={}&" +
                "to={}&Calculate=Convert").format(from_currency, to_currency)
        page = urllib2.urlopen(url).read()

        start = page.rindex('<div id="converter_results"><ul><li>')
        substring = page[start:]
        start_of_interesting_stuff = substring.index('<b>') + 3
        end_of_interesting_stuff = substring.index('</b>', start_of_interesting_stuff)
        interesting_stuff = substring[start_of_interesting_stuff:end_of_interesting_stuff]
        parts = interesting_stuff.split('=')
        value = parts[1].strip().split(' ')[0]
        return float(value)


def currency_symbols():
    return _currency_rates.currency_symbols()

def conversion_rate(from_currency, to_currency):
    return _currency_rates.get_rate(from_currency, to_currency)

_currency_rates = CurrencyRates()
