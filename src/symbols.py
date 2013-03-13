import urllib2, re
from datetime import datetime

class SymbolsRetriever:
    def __init__(self):
        self.cached_symbols = None
        self.last_updated = datetime.min


    def get_symbols(self):
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


