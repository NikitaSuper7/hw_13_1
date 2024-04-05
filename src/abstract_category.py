from abc import ABC, abstractmethod


class AbstractCategory(ABC):

    @abstractmethod
    def __init__(self):
        pass


    @abstractmethod
    def pud_products(self, arg):
        pass
