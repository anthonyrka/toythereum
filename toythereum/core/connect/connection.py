from abc import ABC, abstractmethod
from web3 import Web3

class Connection(ABC):
    def __init__(cls, provider):
        cls.provider = provider

    @abstractmethod
    def resolve(cls):
        pass

    @abstractmethod
    def isConnected(cls):
        pass

class HTTPConnection(Connection):
    def resolve(cls):
        try:
            conn = Web3(Web3.HTTPProvider(cls.provider.endpoint))
            if cls.isConnected(conn):
                return conn
            else:
                raise ValueError('Unable to network over HTTP')
        except:
            raise ValueError('Something went wrong while establishing an HTTP connection')

    def isConnected(cls, conn):
        return conn.isConnected()