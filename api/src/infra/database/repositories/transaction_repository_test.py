from src.domain.entities.transaction import Transaction
from src.services.contracts.transaction_repository_contract import TransactionRepositoryContract


class TransactionRepositoryTest(TransactionRepositoryContract):

    def save_transaction(self, transaction: Transaction) -> Transaction:
        return transaction
