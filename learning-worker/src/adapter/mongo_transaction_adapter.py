from typing import Dict

from src.core.entity.transaction import Transaction

def mongo_transaction_adapter(mongo_obj: Dict) -> Transaction:
    transaction = Transaction()
    transaction.internal_id = mongo_obj['_id']
    transaction.transaction_id = mongo_obj['transactionId']
    transaction.merchant_id = mongo_obj['merchantId']
    transaction.user_id = mongo_obj['userId']
    transaction.card_number = mongo_obj['cardNumber']
    transaction.date = mongo_obj['transactionDate']
    transaction.amount = mongo_obj['transactionAmount']
    transaction.device_id = mongo_obj['deviceId']
    transaction.is_fraud = mongo_obj['isFraud']

    return transaction