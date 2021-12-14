from abc import ABC, abstractmethod
from typing import Dict, List

from src.domain.entities.predict import Predict
from src.domain.entities.transaction import Transaction
from src.domain.entities.learning_model import LearningModel

class MachineLearningContract(ABC):

    @abstractmethod
    def predict(self, learning_model: LearningModel, transaction: Transaction) -> Predict:
        pass
