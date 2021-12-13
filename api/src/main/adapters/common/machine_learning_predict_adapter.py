from typing import List
from sklearn.preprocessing import StandardScaler, LabelEncoder


from src.domain.entities.transaction import Transaction

def machine_learning_predict_adapter(transaction: Transaction) -> List[List[float]]:
    
    return [[
        transaction.merchant_id,
        transaction.user_id,
        transaction.transaction_amount,
        transaction.device_id,
    ]]
