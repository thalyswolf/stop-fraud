from fastapi import FastAPI, Response

from src.domain.usecase.request_and_response import *
from src.main.adapters.http.fast_api_adapter import fast_api_adapter
from src.services.controller.check_transaction_controller import CheckTransactionController
from src.services.controller.update_transaction_controller import UpdateTransactionController


app = FastAPI()

# @app.post('/check-transaction', response_model=CheckTransactionResponse)
@app.post('/check-transaction')
def check_transaction(body: CheckTransactionRequest, response: Response) -> CheckTransactionResponse:

    request = {
        'body': body,
        'headers': None,
        'query': None
    }
    result = CheckTransactionController().check_transaction(fast_api_adapter(request))
    response.status_code = result.status_code
    
    return result.body


# @app.post('/update-transaction', response_model=UpdateTransactionResponse)
@app.post('/update-transaction')
def update_transaction(body: UpdateTransactionRequest, response: Response) -> UpdateTransactionResponse:

    request = {
        'body': body,
        'headers': None,
        'query': None
    }
    result = UpdateTransactionController().update_transaction(fast_api_adapter(request))
    response.status_code = result.status_code

    return result.body
