from abc import ABC, abstractmethod
from typing import Dict, List

from src.domain.entities.predict import Predict
from src.domain.entities.transaction import Transaction


class MachineLearningContract(ABC):

    @abstractmethod
    def predict(self, transaction: Transaction) -> Predict:
        pass
