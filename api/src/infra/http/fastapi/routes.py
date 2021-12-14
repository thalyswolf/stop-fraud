from fastapi import FastAPI, Response

from src.domain.usecase.request_and_response import *
from src.main.adapters.http.fast_api_adapter import fast_api_adapter
from src.services.controller.check_transaction_controller import CheckTransactionController
from src.services.controller.update_transaction_controller import UpdateTransactionController


app = FastAPI()

@app.post('/check-transaction', response_model=CheckTransactionResponse)
def check_transaction(body: CheckTransactionRequest, response: Response) -> CheckTransactionResponse:

    request = {
        'body': body,
        'headers': None,
        'query': None
    }
    response = CheckTransactionController().check_transaction(fast_api_adapter(request))

    print(response.body)
    return response.body


@app.post('/update-transaction', response_model=UpdateTransactionResponse)
def update_transaction(body: UpdateTransactionRequest, response: Response) -> UpdateTransactionResponse:

    request = {
        'body': body,
        'headers': None,
        'query': None
    }
    response = UpdateTransactionController().update_transaction(fast_api_adapter(request))

    print(response.body)
    return response.body
