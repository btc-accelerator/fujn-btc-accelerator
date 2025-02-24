import requests

def check_transaction(txid):
    url = f"https://mempool.space/api/tx/{txid}"
    response = requests.get(url)
    
    if response.status_code == 200:
        tx_data = response.json()
        return f"Transaction {txid} found. Confirmations: {tx_data.get('status', {}).get('confirmed', 'Pending')}"
    else:
        return "Transaction not found or still in mempool."

txid = input("Enter your Bitcoin transaction ID: ")
print(check_transaction(txid))
