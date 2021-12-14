from src.core.usecase.to_learning_usecase import ToLearningUsecase
from src.helpers.csv import CSV
from src.infra.database.repository.transaction_repository_test import TransactionRepositoryTest
from src.infra.database.repository.model_repository_test import ModelRepositoryTest
from src.infra.database.repository.model_repository_mongo import ModelRepositoryMongo
from src.helpers.machine_learning import MachineLearning


class ToLearningController:

    def to_learning(self):
        ToLearningUsecase(CSV(), MachineLearning(), TransactionRepositoryTest(), ModelRepositoryMongo()).execute()
