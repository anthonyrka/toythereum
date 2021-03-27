from abc import ABC, abstractmethod

class Provider(ABC):
    def __init__(cls):
        pass

    @abstractmethod
    def resolve(cls):
        pass