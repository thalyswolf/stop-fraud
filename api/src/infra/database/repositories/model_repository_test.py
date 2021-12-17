from src.services.contracts.model_repository_contract import ModelRepositoryContract
from src.domain.entities.learning_model import LearningModel

class ModelRepositoryTest(ModelRepositoryContract):

    def get_last_learned_model(self) -> LearningModel:
        model = LearningModel()
        model.model = ''
        return model
