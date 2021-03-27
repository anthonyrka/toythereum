```
python3 -m venv venv
source venv/bin/activate

https://web3py.readthedocs.io/en/latest/quickstart.html
pip install web3

#https://geth.ethereum.org/docs/install-and-build/installing-geth
# choose this option if patience and you have disk space
docker pull ethereum/client-go
docker run -p 8545:8545 --name geth ethereum/client-go --rpc --rpcaddr 0.0.0.0
w3 = Web3(Web3.HTTPProvider('http://0.0.0.0:8545'))
>>> w3.isConnected()
True

# Otherwise sign up with infura for free
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/<GET-YOUR-OWN-FROM-INFURA>'))
address = '<YOUR ADDRESS>'
bal = w3.eth.get_balance(address)
>>> w3.fromWei(bal, 'ether')
Decimal('0.01179221')

#create a wallet
https://ethereum.stackexchange.com/questions/32940/how-can-i-generate-a-wallet-in-python/33123
```
