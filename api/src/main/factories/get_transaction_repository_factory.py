from src.infra.database.repositories.transaction_repository_mongo import TransactionRepositoryMongo

def get_transaction_repository_factory():
    return TransactionRepositoryMongo()
