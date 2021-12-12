from typing import Dict

from src.domain.entities.transaction import Transaction
from src.domain.usecase.check_transaction import CheckTransactionRequest
from src.services.contracts.machine_learning_contract import MachineLearningContract

class CheckTransactionUsecase:
    
    def __init__(self, machine_learning: MachineLearningContract) -> None:
        self._machine_learning = machine_learning

    def execute(self, request: CheckTransactionRequest) -> Dict:

        transaction = Transaction()
        transaction.transaction_id = request.transactionId
        transaction.user_id = request.userId
        transaction.card_number = request.cardNumber 
        transaction.transaction_date = request.transactionDate
        transaction.transaction_amount = request.transactionAmount
        transaction.device_id = request.deviceId
        transaction.merchant_id = request.merchantId


        predict = self._machine_learning.predict(transaction)

        return {
            'transactionId': transaction.transaction_id,
            'recommendation': predict.status
        }
