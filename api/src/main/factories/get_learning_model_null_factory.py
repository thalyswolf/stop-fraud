from src.domain.entities.learning_model import LearningModel

def get_learning_model_null_factory():
    learning_model = LearningModel()
    learning_model.model = None
    return learning_model
