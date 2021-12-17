from abc import ABC, abstractmethod

from src.domain.entities.transaction import Transaction


class TransactionRepositoryContract(ABC):

    @abstractmethod
    def save_transaction(self, transaction: Transaction) -> Transaction:
        pass

    @abstractmethod
    def save_new_status(self, internal_id: str, new_status: bool):
        pass
