import urllib.parse
import urllib.request
from typing import Any, Dict


class SingletonType(type):
    _instances: Dict[type, type] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class URLFetcher(metaclass=SingletonType):
    def __init__(self):
        self.urls = []

    def fetch(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)
        urls = self.urls
        urls.append(url)
        self.urls = urls

    def dump_url_registry(self):
        return ", ".join(self.urls)


def main():
    MY_URLS = ["http://www.voidspace.org.uk", "http://google.com", "http://python.org", "https://www.python.org/error"]
    print(URLFetcher() is URLFetcher())

    fetcher = URLFetcher()
    for url in MY_URLS:
        try:
            fetcher.fetch(url)
        except Exception as e:
            print(e)

    print("---------")
    done_urls = fetcher.dump_url_registry()
    print(f"Done URLs: {done_urls}")


if __name__ == "__main__":
    main()
