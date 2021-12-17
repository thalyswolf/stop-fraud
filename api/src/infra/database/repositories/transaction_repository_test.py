from uuid import uuid4

from src.domain.entities.transaction import Transaction
from src.services.contracts.transaction_repository_contract import TransactionRepositoryContract

class TransactionRepositoryTest(TransactionRepositoryContract):

    def save_transaction(self, transaction: Transaction) -> Transaction:
        transaction.internal_id = str(uuid4())
        return transaction


    def save_new_status(self, internal_id: str, new_status: bool):
        pass
