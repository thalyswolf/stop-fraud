from src.contract.csv_contract import CSVContract
from src.contract.transaction_repository_contract import TransactionRepositoryContract
from src.contract.machine_learning_contract import MachineLearningContract
from src.contract.model_repository_contract import ModelRepositoryContract

class ToLearningUsecase:

    def __init__(self,
                machine_learning: MachineLearningContract,
                transaction_repository: TransactionRepositoryContract,
                model_repository: ModelRepositoryContract
                ) -> None:
        self._transaction_repository = transaction_repository
        self._machine_learning = machine_learning
        self._model_repository = model_repository


    def execute(self):
        transactions_db = self._transaction_repository.list()
        self._machine_learning.preprocessing(transactions_db)
        model = self._machine_learning.learning()

        self._model_repository.save(model)
