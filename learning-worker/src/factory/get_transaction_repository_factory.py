from src.infra.database.repository.transaction_repository_mongo import TransactionRepositoryMongo


def get_transaction_repository_factory():
    return TransactionRepositoryMongo()
