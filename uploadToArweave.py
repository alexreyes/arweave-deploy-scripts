from arweave.arweave_lib import Wallet, Transaction

import arweave


wallet_file_path = "quarantine-journal-keyfile.json"
wallet = arweave.Wallet(wallet_file_path)

balance = wallet.balance 
address = wallet.address
# print(balance)
print(address)
last_transaction = wallet.get_last_transaction_id()
# print(last_transaction)


with open('metadata.json', 'r') as myMetadata:
	metadata_string_data = myMetadata.read()

	theData = '<html><head><meta charset="UTF-8"><title>MDNFT Metadata</title></head><body>' + metadata_string_data +'</body></html>'
	transaction = Transaction(wallet, data=theData)
	transaction.sign()
	transaction.send()

