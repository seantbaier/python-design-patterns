import abc


class MapSite(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def enter(self):
        raise NotImplementedError
