from time import time

from src.contract.model_repository_contract import ModelRepositoryContract
from src.infra.database.mongo.connection import MongoConnection

class ModelRepositoryMongo(ModelRepositoryContract):

    def __init__(self) -> None:
        database = MongoConnection().get_database()
        self.collection_name = database['models']

    def save(self, model: bytes):
        result = self.collection_name.insert_one({
            'model': model,
            'createdAt': int(time())
        })

    def get_last_inserted(self) -> bytes:
        result = self.collection_name.find_one({
            'createdAt': 1639493197
        })

        return result['model']
