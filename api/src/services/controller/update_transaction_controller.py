from traceback import format_exc

from src.services.enum.http_status_enum import HTTPResponseStatus
from src.services.usecase.update_transaction.update_transaction_usecase import UpdateTransactionUsecase
from src.services.contracts.controller_contract import HttpRequest, HttpResponse
from src.main.factories.get_transaction_repository_factory import get_transaction_repository_factory
from src.main.factories.get_messaging_queue_factory import get_messaging_queue_factory
from src.services.errors.handler import *


class UpdateTransactionController:
    
    def update_transaction(self, http_request: HttpRequest) -> HttpResponse:
        try:

            transaction_repository = get_transaction_repository_factory()
            messaging_queue = get_messaging_queue_factory()

            response = UpdateTransactionUsecase(transaction_repository, messaging_queue)\
                                            .execute(http_request.payload)

            return HttpResponse(HTTPResponseStatus.SUCCESS_NO_BODY, response)

        except (InvalidAmountErrorException, InvalidRecommendationErrorException) as ie:
            return HttpResponse(HTTPResponseStatus.INVALID_DATA, {
                'error': ie.message
            })
        
        except NotFoundDBErrorException as ne:
            return HttpResponse(HTTPResponseStatus.NOT_FOUND, {
                'error': ne.message
            })

        except Exception:
            return HttpResponse(HTTPResponseStatus.ERROR, {
                'error': format_exc()
            })
