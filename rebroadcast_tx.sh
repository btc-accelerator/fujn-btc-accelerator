#!/bin/bash

echo "Enter your Bitcoin transaction ID:"
read txid

curl -X POST "https://mempool.space/api/tx" -d "$txid"

echo "Transaction rebroadcasted. Check status on Mempool.space."
