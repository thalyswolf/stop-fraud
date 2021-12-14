from abc import ABC, abstractmethod
from typing import List

from src.core.entity.transaction import Transaction

class CSVContract(ABC):

    @abstractmethod
    def read_csv(self):
        pass


    @abstractmethod
    def write_row(self, transactions:List[Transaction]):
        pass
