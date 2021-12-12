from src.services.usecase.check_transaction.check_transaction_usecase import CheckTransactionUsecase
from src.presentation.contracts.controller_contract import HttpRequest, HttpResponse


class CheckTransactionController:
    
    def check_transaction(self, http_request: HttpRequest) -> HttpResponse:
        response = CheckTransactionUsecase().execute(http_request.payload)
