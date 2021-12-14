from abc import ABC, abstractmethod
from typing import List

from src.core.entity.transaction import Transaction

class MachineLearningContract(ABC):

    @abstractmethod
    def preprocessing(self) -> None:
        pass

    @abstractmethod
    def learning(self) -> None:
        pass
