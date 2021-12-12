from typing import List
from sklearn.preprocessing import StandardScaler, LabelEncoder


from src.domain.entities.transaction import Transaction

def machine_learning_predict_adapter(transaction: Transaction) -> List[List[float]]:
    card_number_label_encoder = LabelEncoder()
    card_number_label_encoder.fit_transform([transaction.card_number])
    values = card_number_label_encoder.transform(card_number_label_encoder.classes_)
    
    return [[
        transaction.merchant_id,
        transaction.user_id,
        values[0],
        transaction.transaction_amount,
        transaction.device_id,
    ]]
