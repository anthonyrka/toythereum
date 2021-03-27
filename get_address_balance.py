from toythereum.core.connect.provider import HTTPProvider
from toythereum.core.connect.connection import HTTPConnection
import sys

if __name__ == '__main__':
    provider_account_num = sys.argv[1]
    address = sys.argv[2]
    provider_uri = sys.argv[3]

    uri = f"{provider_uri}/{provider_account_num}"

    net = HTTPConnection(HTTPProvider(uri)).resolve()
    bal = net.eth.get_balance(address)

    print(f"Crypto Address: {address}\nBalance: {net.fromWei(bal, 'ether')} ether")