from fastapi import FastAPI, Response

from src.domain.usecase.check_transaction import CheckTransactionRequest, CheckTransactionResponse
from src.main.adapters.http.fast_api_adapter import fast_api_adapter
from src.presentation.controller.check_transaction import CheckTransactionController

app = FastAPI()

@app.post('/check-transaction', response_model=CheckTransactionResponse)
def check_transaction(body: CheckTransactionRequest, response: Response) -> CheckTransactionResponse:

    try:
        request = {
            'body': body,
            'headers': None,
            'query': None
        }
        response = CheckTransactionController().check_transaction(fast_api_adapter(request))

        return {
            'transaction_id': 1,
            'recommendation': 'approve'
        }
        
    except:
        from traceback import format_exc
        print(format_exc())