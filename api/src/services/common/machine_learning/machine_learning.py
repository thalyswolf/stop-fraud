import pickle, os

from src.main.adapters.common.machile_learning_decode_adapter import machine_learning_decode_adapter
from src.main.adapters.common.machine_learning_predict_adapter import machine_learning_predict_adapter
from src.domain.entities.transaction import Transaction
from src.domain.entities.predict import Predict
from src.domain.entities.learning_model import LearningModel

class MachineLearning:

    def __init__(self) -> None:
        self._pickle = pickle


    def predict(self, learning_model: LearningModel, transaction: Transaction) -> Predict:

        if learning_model.model:
            objekt = self._pickle.loads(learning_model.model)
        else: 
            with open(os.path.dirname(os.path.abspath(__file__)) + '/model.pkl', 'rb') as f:
                objekt = pickle.load(f)
            
        response_predict = objekt.predict(machine_learning_predict_adapter(transaction))
        
        return machine_learning_decode_adapter(response_predict)
