from typing import Dict

from src.domain.usecase.request_and_response import UpdateTransactionRequest
from src.services.contracts.transaction_repository_contract import TransactionRepositoryContract
from src.services.contracts.messaging_queue_contract import MessagingQueueContract

class UpdateTransactionUsecase:
    
    def __init__(self,transaction_repository: TransactionRepositoryContract, messaging_queue: MessagingQueueContract) -> None:
        self._transaction_repository = transaction_repository
        self._messaging_queue = messaging_queue

    def execute(self, request: UpdateTransactionRequest) -> Dict:
        internal_id = request.internalId
        is_fraud = True if request.newRecommendation == 'deny' else False
        self._transaction_repository.save_new_status(internal_id, is_fraud)

        self._messaging_queue.send_to_queue()
