import urllib2, re
from datetime import datetime

class SymbolsRetriever:
    def get_symbols(self):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        url = "http://www.xe.com/iso4217.php" 
        page = opener.open(url).read()

        symbols = {}
        currency_regex = r'href="/currency/[^>]+>(...)</a></td><td class="[^"]+">([A-Za-z ]+)'
        for m in re.finditer(currency_regex, page):
            symbols[m.group(1)] = m.group(2)

        return symbols


class CachingSymbolsRetriever:
    def __init__(self, decorated_retriever):
        self.cached_symbols = None
        self.last_updated = datetime.min
        self.decorated_retriever = decorated_retriever

    def get_symbols(self):
        delta = datetime.now() - self.last_updated
        if self.cached_symbols is None or delta.seconds > 300:
            self.cached_symbols = self.decorated_retriever.get_symbols()
        self.last_updated = datetime.now()
        return self.cached_symbols
