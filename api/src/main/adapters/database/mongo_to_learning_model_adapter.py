from typing import Dict

from src.domain.entities.learning_model import LearningModel

def mongo_to_learning_model_adapter(model: Dict) -> LearningModel:
    learning_model = LearningModel()
    learning_model.model = model['model']
    return learning_model
