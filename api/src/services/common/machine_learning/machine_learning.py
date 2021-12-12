from typing import Dict, List
import pickle
from sklearn.naive_bayes import GaussianNB
import os.path

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
        predict = Predict()
        predict.status = 'approve'
        return predict
