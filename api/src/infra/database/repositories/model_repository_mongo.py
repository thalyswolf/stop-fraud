import pymongo

from src.services.contracts.model_repository_contract import ModelRepositoryContract
from src.infra.database.mongo.connection import MongoConnection
from src.domain.entities.learning_model import LearningModel
from src.main.adapters.database.mongo_to_learning_model_adapter import mongo_to_learning_model_adapter
from src.services.errors.handler import NotFoundDBErrorException

class ModelRepositoryMongo(ModelRepositoryContract):

    def __init__(self) -> None:
        database = MongoConnection().get_database()
        self.collection_name = database['models']


    def get_last_learned_model(self) -> LearningModel:
        result = self.collection_name.find().sort("createdAt", pymongo.DESCENDING)

        if result.count() == 0:
            raise NotFoundDBErrorException()

        return mongo_to_learning_model_adapter(result[0])
                   
