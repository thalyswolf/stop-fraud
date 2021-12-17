from src.infra.database.repositories.model_repository_mongo import ModelRepositoryMongo

def get_model_repository_factory():
    return ModelRepositoryMongo()
