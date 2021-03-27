from web3 import Web3

if __name__ == '__main__':
    provider_account_num = '<GET-YOUR-OWN-FROM-INFURA>'
    provider_url = f'https://mainnet.infura.io/v3/{provider_account_num}'
    w3 = Web3(Web3.HTTPProvider(provider_url))
    address = '0x7829e7bDc86dEc3f00403f7E6b58aa8d42d86cF7'
    bal = w3.eth.get_balance(address)
    print(f"Account Number: {address}\nBalance: {w3.fromWei(bal, 'ether')}")
