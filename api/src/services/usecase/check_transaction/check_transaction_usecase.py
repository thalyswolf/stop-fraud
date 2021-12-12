from typing import Dict


class CheckTransactionUsecase:
    
    def execute(self, request: Dict) -> Dict:
        print('chegou no usecase')