from abc import ABC, abstractmethod
from web3 import Web3

class Provider(ABC):
    pass

class HTTPProvider(Provider):
    def __init__(cls, endpoint):
        cls.endpoint = endpoint