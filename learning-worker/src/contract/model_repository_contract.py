from abc import ABC, abstractmethod
from typing import List


class ModelRepositoryContract(ABC):

    @abstractmethod
    def save(self, model: bytes):
        pass
