from abc import ABC, abstractmethod

from src.domain.entities.learning_model import LearningModel


class ModelRepositoryContract(ABC):

    @abstractmethod
    def get_last_learned_model(self) -> LearningModel:
        pass
