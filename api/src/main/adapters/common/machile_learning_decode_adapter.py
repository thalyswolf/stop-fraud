from typing import List
from src.domain.entities.predict import Predict
from src.services.enum.recommendation_enum import APPROVE, DENY


def machine_learning_decode_adapter(predict_response: List[bool]) -> Predict:
    predict = Predict()
    predict.status = APPROVE if not predict_response[0] else DENY
    return predict
