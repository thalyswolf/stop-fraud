from typing import Dict

from src.services.errors.handler import InvalidAmountErrorException
from src.domain.entities.transaction import Transaction
from src.domain.usecase.request_and_response import CheckTransactionRequest
from src.services.contracts.machine_learning_contract import MachineLearningContract
from src.services.contracts.transaction_repository_contract import TransactionRepositoryContract
from src.services.contracts.model_repository_contract import ModelRepositoryContract

class CheckTransactionUsecase:
    
    def __init__(self, machine_learning: MachineLearningContract, 
                transaction_repository: TransactionRepositoryContract,
                model_repository: ModelRepositoryContract) -> None:
        self._machine_learning = machine_learning
        self._transaction_repository = transaction_repository
        self._model_repository = model_repository

    def execute(self, request: CheckTransactionRequest) -> Dict:

        amount = request.transactionAmount

        if float(amount) < 0:
            raise InvalidAmountErrorException()

        transaction = Transaction()
        transaction.transaction_id = request.transactionId
        transaction.user_id = request.userId
        transaction.card_number = request.cardNumber 
        transaction.date = request.transactionDate
        transaction.amount = amount
        transaction.device_id = request.deviceId
        transaction.merchant_id = request.merchantId

        model_learned = self._model_repository.get_last_learned_model()

        predict = self._machine_learning.predict(model_learned, transaction)

        transaction.is_fraud = True if predict.status == 'deny' else False

        _ = self._transaction_repository.save_transaction(transaction)

        print(transaction.internal_id)

        return {
            'transactionId': transaction.transaction_id,
            'recommendation': predict.status,
            'internalId': transaction.internal_id
        }
