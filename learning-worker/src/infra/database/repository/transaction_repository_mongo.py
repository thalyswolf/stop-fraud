from typing import List

from src.contract.transaction_repository_contract import TransactionRepositoryContract
from src.core.entity.transaction import Transaction
from src.infra.database.mongo.connection import MongoConnection
from src.adapter.mongo_transaction_adapter import mongo_transaction_adapter

class TransactionRepositoryMongo(TransactionRepositoryContract):

    def __init__(self) -> None:
        database = MongoConnection().get_database()
        self.collection_name = database['transactions']


    def list(self) -> List[Transaction]:
        results = self.collection_name.find()

        return list(map(mongo_transaction_adapter, results))
