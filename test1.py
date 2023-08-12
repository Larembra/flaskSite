from web3 import Web3


infura_url = "https://mainnet.infura.io/v3/ba397cc388294a1d8e86ddeadcb62391"
ganache_url = "HTTP://127.0.0.1:7545"


w3 = Web3(Web3.HTTPProvider(ganache_url))
# w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

account_address = "0x6BB441f9D8F30678264f0524638DA11de1e1B571" # адрес аккаунта, с которого производится транзакция ganache

w3.eth.default_account = account_address

contract_address = "0xd9145CCE52D386f254917e481eB44e9943F39138"

# print(w3.eth.getBalance("account_address"))

abi = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "email",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "login",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "password",
				"type": "uint256"
			}
		],
		"name": "addNewUser",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint8",
				"name": "newAge",
				"type": "uint8"
			},
			{
				"internalType": "address",
				"name": "id",
				"type": "address"
			}
		],
		"name": "setAge",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "newEmail",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "id",
				"type": "address"
			}
		],
		"name": "setEmail",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "newLogin",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "id",
				"type": "address"
			}
		],
		"name": "setLogin",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "newName",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "id",
				"type": "address"
			}
		],
		"name": "setName",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "oldPassword",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "newPassword",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "id",
				"type": "address"
			}
		],
		"name": "setPassword",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "id",
				"type": "address"
			}
		],
		"name": "deleteUserByID",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "id",
				"type": "address"
			}
		],
		"name": "getUserByID",
		"outputs": [
			{
				"internalType": "contract User",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

contract = w3.eth.contract(address=contract_address, abi=abi)
# contract.deploy({'from': 0xf36EB59B8FADAd3598084717669f81c6E83E7D1A, 'gasPrice': w3.eth.gasPrice, 'gas': w3.eth.getBlock('latest').gasLimit})

a = contract.caller.address

# Добавление нового имени в базу данных
tx_hash = contract.functions.addNewUser("Sjt", "yrtt", 19).transact({'from': account_address})
# насчет транзакта, нееросеть сказала, в нем нужен адрес вызывающего функцию, у меня была ошибка с тем, что
# print(tx_hash)
# print(type(tx_hash))

receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print(receipt.status)

# # Wait for the transaction to be mined
# tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
#
# # Retrieve the contract address from the transaction receipt
# ca = tx_receipt.contractAddress

# Вызов метода контракта
names = contract.functions.getUserByID(contract.caller.address).transact({'from': contract.caller.address})

events = contract.events.UserReturned().processReceipt(names)

print(events)

# Получение статуса транзакции
receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print(receipt.status)