import pytest
from faker import Faker
from unittest import TestCase

from src.services.enum.recommendation_enum import APPROVE, DENY
from src.infra.database.repositories.transaction_repository_test import TransactionRepositoryTest
from src.infra.queue.rabbitmq.rabbitmq_test import RabbitMQMessagingTest
from src.services.usecase.update_transaction.update_transaction_usecase import UpdateTransactionUsecase
from src.services.errors.handler import InvalidRecommendationErrorException


faker = Faker()

def make_sut_request_approve():
    class Request():
        internalId = faker.word()
        newRecommendation = APPROVE

    return Request()

def make_sut_request_deny():
    class Request():
        internalId = faker.word()
        newRecommendation = DENY

    return Request()

def make_sut_transaction_repository():
    return TransactionRepositoryTest()

def make_sut_messaging_queue():
    return RabbitMQMessagingTest()

def test_should_raise_invalid_new_status():
    request = make_sut_request_deny()
    request.newRecommendation = faker.word()
    with pytest.raises(InvalidRecommendationErrorException):
        _ = UpdateTransactionUsecase(make_sut_transaction_repository(), make_sut_messaging_queue()).execute(request)

def test_should_success_if_new_recommendation_is_approve():
    request = make_sut_request_approve()
    _ = UpdateTransactionUsecase(make_sut_transaction_repository(), make_sut_messaging_queue()).execute(request)

def test_should_success_new_recommendation_is_deny():
    request = make_sut_request_deny()
    _ = UpdateTransactionUsecase(make_sut_transaction_repository(), make_sut_messaging_queue()).execute(request)
