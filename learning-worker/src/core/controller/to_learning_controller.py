from src.core.usecase.to_learning_usecase import ToLearningUsecase
from src.infra.database.repository.transaction_repository_test import TransactionRepositoryTest
from src.infra.database.repository.model_repository_mongo import ModelRepositoryMongo
from src.helpers.machine_learning import MachineLearning
from src.factory.get_machine_learning_factory import get_machine_learning_factory
from src.factory.get_model_repository_factory import get_model_repository_factory
from src.factory.get_transaction_repository_factory import get_transaction_repository_factory

class ToLearningController:

    def to_learning(self):
        machine_learning = get_machine_learning_factory()
        transaction_repository = get_transaction_repository_factory()
        model_repository = get_model_repository_factory()

        ToLearningUsecase(machine_learning, transaction_repository, model_repository).execute()
