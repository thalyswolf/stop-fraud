from typing import List
from sklearn.preprocessing import StandardScaler, LabelEncoder


from src.domain.entities.transaction import Transaction
from src.services.helpers.amount import format_amount_from_int_to_float

def machine_learning_predict_adapter(transaction: Transaction) -> List[List[float]]:
    
    return [[
        transaction.merchant_id,
        transaction.user_id,
        transaction.amount,
        transaction.device_id,
    ]]
