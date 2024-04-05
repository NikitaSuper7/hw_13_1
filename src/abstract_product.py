from abc import ABC, abstractmethod


class AbstrProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    #@classmethod
    def build_product(self, dict):
        pass
