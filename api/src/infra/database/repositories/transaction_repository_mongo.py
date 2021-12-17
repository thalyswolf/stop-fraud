from bson.objectid import ObjectId

from src.domain.entities.transaction import Transaction
from src.services.contracts.transaction_repository_contract import TransactionRepositoryContract
from src.infra.database.mongo.connection import MongoConnection
from src.services.errors.handler import NotFoundDBErrorException

class TransactionRepositoryMongo(TransactionRepositoryContract):

    def __init__(self) -> None:
        database = MongoConnection().get_database()
        self.collection_name = database['transactions']

    def save_transaction(self, transaction: Transaction) -> Transaction:
        transaction_data = {
            'transactionId': transaction.transaction_id,
            'userId': transaction.user_id,
            'cardNumber': transaction.card_number,
            'transactionDate': transaction.date,
            'transactionAmount': transaction.amount,
            'deviceId': transaction.device_id,
            'merchantId': transaction.merchant_id,
            'isFraud': transaction.is_fraud
        }

        result = self.collection_name.insert_one(transaction_data)

        transaction.internal_id = str(result.inserted_id)

        return transaction

    def save_new_status(self, internal_id: str, new_status: bool):
        print(new_status)
        query = { "_id": ObjectId(internal_id) }

        check = self.collection_name.find_one(query)

        if not check:
            raise NotFoundDBErrorException()

        result = self.collection_name.find_one_and_update(query, { "$set": {'isFraud': new_status} }, upsert=False)

        print(result)

