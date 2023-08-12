from web3 import Web3
import json
# infura_url = "https://mainnet.infura.io/v3/ba397cc388294a1d8e86ddeadcb62391"
# web3 = Web3(Web3.HTTPProvider(infura_url))
# print(web3.isConnected())
# print(web3.eth.blockNumber)
#
# balance = web3.eth.getBalance("0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC")
# web3.fromWei(balance, 'ether')
# print(balance)
ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.defaultAccount = web3.eth.accounts[0]
abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"string","name":"email","type":"string"},{"internalType":"string","name":"login","type":"string"},{"internalType":"uint256","name":"password","type":"uint256"}],"name":"addNewUser","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"id","type":"address"}],"name":"deleteUserByID","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"id","type":"address"}],"name":"getUserByID","outputs":[{"internalType":"contract User","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"newAge","type":"uint8"},{"internalType":"address","name":"id","type":"address"}],"name":"setAge","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"newEmail","type":"string"},{"internalType":"address","name":"id","type":"address"}],"name":"setEmail","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"newLogin","type":"string"},{"internalType":"address","name":"id","type":"address"}],"name":"setLogin","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"newName","type":"string"},{"internalType":"address","name":"id","type":"address"}],"name":"setName","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"oldPassword","type":"uint256"},{"internalType":"uint256","name":"newPassword","type":"uint256"},{"internalType":"address","name":"id","type":"address"}],"name":"setPassword","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"nonpayable","type":"function"}]')

address =web3.toChecksumAddress("0xc88d38c62Dc4B2761072f4D3729130A4eeC3fa0E")  # как получать этот адресс из ремикса напрямую?
contract = web3.eth.contract(address = address, abi = abi)
# print(contract.functions.getUserByID("0x517DFd14d6A76ff9B74147d0611d054989eCf485").call())
print(contract.functions.addNewUser("Sjt", "yrtt", 19).call())
#tx_hash = contract.functions.setGreeting('HHHHHHEEEEEELLLLOOOOOOOOOOO!').transact()
#print(tx_hash)
#web3.eth.waitForTransactionReceipt(tx_hash)
#print('Updated greeting: {}'.format(
# contract.functions.greet().call()
# ))
#Используя последние 6 строк, он смог изменить значение, вводимое в контракт. Походу, нужны одиночные скобки.