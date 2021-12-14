from typing import List

from src.contract.transaction_repository_contract import TransactionRepositoryContract
from src.core.entity.transaction import Transaction

class TransactionRepositoryTest(TransactionRepositoryContract):

    def _get_transactions(self):
        transaction = Transaction()
        transaction.transaction_id = 1
        transaction.merchant_id = 1
        transaction.user_id = 99999999
        transaction.card_number = 'cccc'
        transaction.date = 'cccc'
        transaction.amount = 10.0
        transaction.device_id = '1'
        transaction.is_fraud = False

        transaction2 = Transaction()
        transaction2.transaction_id = 2
        transaction2.merchant_id = 2
        transaction2.user_id = 88888888
        transaction2.card_number = 'xxxxx'
        transaction2.date = 'xxxxx'
        transaction2.amount = 20.0
        transaction2.device_id = '2'
        transaction2.is_fraud = True

        return [transaction, transaction2]

    def list(self) -> List[Transaction]:
        return self._get_transactions()


