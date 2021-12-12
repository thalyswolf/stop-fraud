from typing import Dict

from src.domain.entities.transaction import Transaction
from src.domain.usecase.check_transaction import CheckTransactionRequest
from src.services.contracts.machine_learning_contract import MachineLearningContract

class CheckTransactionUsecase:
    
    def __init__(self, machine_learning: MachineLearningContract) -> None:
        self._machine_learning = machine_learning

    def execute(self, request: CheckTransactionRequest) -> Dict:

        transaction = Transaction()
        transaction.transaction_id = request.transaction_id
        transaction.user_id = request.user_id
        transaction.card_number = request.card_number 
        transaction.transaction_date = request.transaction_date
        transaction.transaction_amount = request.transaction_amount
        transaction.device_id = request.device_id

        predict = self._machine_learning.predict(transaction)

        return {
            'transaction_id': transaction.transaction_id,
            'recommendation': predict.status
        }
