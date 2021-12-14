from typing import List
from src.core.entity.transaction import Transaction

def transaction_to_list_row_adapter(transaction: Transaction) -> List:
    return [transaction.transaction_id, 
            transaction.merchant_id, 
            transaction.user_id, 
            transaction.card_number,
            transaction.date,
            transaction.amount,
            transaction.device_id,
            transaction.is_fraud
            ]
