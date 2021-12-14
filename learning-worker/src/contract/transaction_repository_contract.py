from abc import ABC, abstractmethod
from typing import List

from src.core.entity.transaction import Transaction

class TransactionRepositoryContract(ABC):

    @abstractmethod
    def list(self) -> List[Transaction]:
        pass
