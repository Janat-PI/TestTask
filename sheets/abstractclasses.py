from abc import ABC, abstractmethod


class AbstractSheet(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    