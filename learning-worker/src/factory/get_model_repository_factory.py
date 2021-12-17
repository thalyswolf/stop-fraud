from src.infra.database.repository.model_repository_mongo import ModelRepositoryMongo


def get_model_repository_factory():
    return ModelRepositoryMongo()