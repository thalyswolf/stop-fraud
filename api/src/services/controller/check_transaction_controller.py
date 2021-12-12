from traceback import format_exc

from src.services.enum.http_status_enum import HTTPResponseStatus
from src.services.usecase.check_transaction.check_transaction_usecase import CheckTransactionUsecase
from src.services.contracts.controller_contract import HttpRequest, HttpResponse
from src.main.factories.get_machine_learning_factory import get_machine_learning_factory

class CheckTransactionController:
    
    def check_transaction(self, http_request: HttpRequest) -> HttpResponse:
        try:
            response = CheckTransactionUsecase(get_machine_learning_factory()).execute(http_request.payload)
            return HttpResponse(HTTPResponseStatus.SUCCESS, response)

        except Exception:
            return HttpResponse(HTTPResponseStatus.ERROR, {
                'message': format_exc()
            })
