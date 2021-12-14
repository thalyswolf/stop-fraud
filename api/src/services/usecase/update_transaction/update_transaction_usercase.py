from typing import Dict

from src.domain.usecase.request_and_response import UpdateTransactionRequest
from src.services.contracts.transaction_repository_contract import TransactionRepositoryContract

class UpdateTransactionUsecase:
    
    def __init__(self,transaction_repository: TransactionRepositoryContract) -> None:
        self._transaction_repository = transaction_repository

    def execute(self, request: UpdateTransactionRequest) -> Dict:
        internal_id = request.internalId
        is_fraud = True if request.newRecommendation == 'deny' else False
        
        print('aqui')

        self._transaction_repository.save_new_status(internal_id, is_fraud)
