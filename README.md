# Toythereum
A simple python implementation useful for checking a crypto wallets ethereum balance on the mainnet. This tutorial leverages the Web3.py [library](https://web3py.readthedocs.io/en/latest/quickstart.html).
## Getting Started
Ensure your development environment is running Python3. For best results I recommend running a python virtual machine (see instructions below).

###Step 1: Clone this repo
Clone the toythereum git repo:
```
# for https:
git clone https://github.com/anthonyrka/toythereum.git
cd toythereum
```
###Step 2: Setup Virtual Environment & Install dependencies
Set up your virtual environment:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements
```
###Step 3: Access the Ethereum mainnet
There are many ways to access the Ethereum mainnet. One way would be to install geth to run as a local ethereum node on your local development machine. However, if you choose this option you should consider the time it will take to download the full blockchain, not to mention the IO, disk space and bandwidth requirements. See https://geth.ethereum.org/docs/install-and-build/installing-geth.

This tutorial wastes no time and leverages an API provider called Infura.io. Visit infura.io to setup a free account. Once signed up (it currently takes 30 seconds), Infura will provide you Endpoints and a ProjectID.

Once you have your PROJECTID and ENDPOINT, set these as local environment variables:
```
export WEB3_INFURA_PROJECT_ID=<YOUR-PROJECT-ID>
export INFURA_MAINNET_URI=https://mainnet.infura.io/v3
```
Note: at the time of this writing, the Infura mainnet can be accessed over HTTP with the above URI. However, you'll want to double-check this is what is provided in your project's account.
###Step 4: Check your wallet's balance of Ether
```
export CRYPTO_WALLET=0x7829e7bDc86dEc3f00403f7E6b58aa8d42d86cF7
python get_address_balance.py $WEB3_INFURA_PROJECT_ID $CRYPTO_WALLET $INFURA_MAINNET_URI

Crypto Address: 0x7829e7bDc86dEc3f00403f7E6b58aa8d42d86cF7
Balance: 0.01179221 ether
```

## Common Issues
If you expect to find a balance in your wallet and you find a 0 result.
There are at least 2 issues to consider:
1. If your wallet is on an exchange such as Coinbase, you will likely not find it on the blockchain. Validate this by searching for your wallet on [etherscan.io](https://etherscan.io/).
2. If you have decided to implement your own geth client locally, the local client is likely still syncing the blockchain. This will take a significant amount of time (maybe multiple days).

##Future
###Creating a wallet:
https://ethereum.stackexchange.com/questions/32940/how-can-i-generate-a-wallet-in-python/33123
