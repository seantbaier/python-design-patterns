import abc
from pathlib import Path
from urllib import request


class ResourceContent:
    """
    Define the abstracton's interface.
    Maintain a reference to an object which represents the Implementor
    """

    def __init__(self, imp):
        self._imp = imp

    def show_content(self, path):
        self._imp.fetch(path)


class ResourceContentFetcher(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def fetch(path):
        pass


class URLFetcher(ResourceContentFetcher):
    def fetch(self, path):
        req = request.Request(path)
        with request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)


class LocalFileFetcher(ResourceContentFetcher):
    def fetch(self, path):
        with open(path) as f:
            print(f.read())


def main():
    url_fetcher = URLFetcher()
    iface = ResourceContent(url_fetcher)
    iface.show_content("http://python.org")

    print("\n==============================\n")

    localfs_fetcher = LocalFileFetcher()
    iface = ResourceContent(localfs_fetcher)
    iface.show_content(Path.cwd().joinpath("./structural_patterns/bridge/file.txt"))


if __name__ == "__main__":
    main()
