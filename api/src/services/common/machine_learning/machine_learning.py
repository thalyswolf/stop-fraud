import pickle, os

from src.main.adapters.common.machile_learning_decode_adapter import machine_learning_decode_adapter
from src.main.adapters.common.machine_learning_predict_adapter import machine_learning_predict_adapter
from src.domain.entities.transaction import Transaction
from src.domain.entities.predict import Predict

class MachineLearning:

    _instance = None
    _objekt = None

    """ Singleton Pattern """
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance


    def __init__(self) -> None:
        if self._objekt is None:
            with open(os.path.dirname(os.path.abspath(__file__)) + '/model.pkl', 'rb') as f:
                self._objekt = pickle.load(f)


    def predict(self, transaction: Transaction) -> Predict:
        response_predict = self._objekt.predict(machine_learning_predict_adapter(transaction))
        return machine_learning_decode_adapter(response_predict)
