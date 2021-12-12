from typing import List
from src.domain.entities.predict import Predict

PREDICT_STATUS_APPROVE = 'approve'
PREDICT_STATUS_DENY = 'deny'


def machine_learning_decode_adapter(predict_response: List[bool]) -> Predict:
    predict = Predict()
    predict.status = PREDICT_STATUS_APPROVE if not predict_response[0] else PREDICT_STATUS_DENY
    return predict
