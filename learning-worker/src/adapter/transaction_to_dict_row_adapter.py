from typing import List
from src.core.entity.transaction import Transaction

def transaction_to_dict_row_adapter(transaction: Transaction) -> List:
    return {
            'transaction_id': transaction.transaction_id,
            'merchant_id': transaction.merchant_id,
            'user_id': transaction.user_id,
            'card_number': transaction.card_number,
            'transaction_date': transaction.date,
            'transaction_amount': transaction.amount,
            'device_id': transaction.device_id,
            'has_cbk': transaction.is_fraud
        }
