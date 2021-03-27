from toythereum.core.infura_provider import InfuraProvider
import sys

if __name__ == '__main__':
    provider_account_num = sys.argv[1]
    address = sys.argv[2]
    provider_uri = sys.argv[3]

    net = InfuraProvider(provider_uri, provider_account_num).resolve()
    bal = net.eth.get_balance(address)

    print(f"Crypto Address: {address}\nBalance: {net.fromWei(bal, 'ether')} ether")