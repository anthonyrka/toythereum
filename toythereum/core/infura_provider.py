from web3 import Web3
from toythereum.core.provider import Provider

class InfuraProvider(Provider):
    def __init__(cls, uri, accountid):
        try:
            cls.uri = uri + '/' + accountid
        except:
            raise ValueError('Something went wrong setting Infura URI')

    def resolve(cls):
        try:
            conn = Web3(Web3.HTTPProvider(cls.uri))
            if cls.isConnected(conn):
                return conn
            else:
                raise ValueError('Unable to connect to Infura mainnet')
        except:
            raise ValueError('Something went wrong connecting to Infura mainnnet')

    def isConnected(cls, conn):
        return conn.isConnected()

