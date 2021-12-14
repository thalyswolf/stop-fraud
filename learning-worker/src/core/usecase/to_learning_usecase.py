from src.contract.csv_contract import CSVContract
from src.contract.transaction_repository_contract import TransactionRepositoryContract
from src.contract.machine_learning_contract import MachineLearningContract
from src.contract.model_repository_contract import ModelRepositoryContract

class ToLearningUsecase:

    def __init__(self, csv: CSVContract,
                machine_learning: MachineLearningContract,
                transaction_repository: TransactionRepositoryContract,
                model_repository: ModelRepositoryContract
                ) -> None:
        self._csv = csv
        self._transaction_repository = transaction_repository
        self._machine_learning = machine_learning
        self._model_repository = model_repository


    def execute(self):
        transactions_db = self._transaction_repository.list()

        _ = self._csv.write_row(transactions_db)
        self._machine_learning.preprocessing()
        model = self._machine_learning.learning()

        self._model_repository.save(model)
        model = self._model_repository.get_last_inserted()
        self._machine_learning.test(model)
        
