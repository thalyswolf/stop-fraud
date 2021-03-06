import pytest
from unittest import TestCase
from faker import Faker

from src.domain.entities.transaction import Transaction
from src.domain.entities.predict import Predict
from src.services.errors.handler import InvalidAmountErrorException
from src.services.usecase.check_transaction.check_transaction_usecase import CheckTransactionUsecase
from src.domain.usecase.request_and_response import CheckTransactionResponse, CheckTransactionRequest
from src.services.contracts.machine_learning_contract import MachineLearningContract
from src.infra.database.repositories.transaction_repository_test import TransactionRepositoryTest
from src.infra.database.repositories.model_repository_test import ModelRepositoryTest


faker = Faker()

APPROVE_TRANSACTION = 'approve'
DENY_TRANSACTION = 'deny'

def make_sut_machine_learning_approve():
    class MachineLearning(MachineLearningContract):
        def predict(self, model_learned, transaction: Transaction) -> Predict:
            response_predict = Predict()
            response_predict.status = APPROVE_TRANSACTION
            return response_predict

    return MachineLearning()

def make_sut_machine_learning_deny():
    class MachineLearning(MachineLearningContract):
        def predict(self, model_learned, transaction: Transaction) -> Predict:
            response_predict = Predict()
            response_predict.status = DENY_TRANSACTION
            return response_predict

    return MachineLearning()

def make_sut_transaction_repository():
    return TransactionRepositoryTest()

def make_sut_model_repository():
    return ModelRepositoryTest()

def make_sut_request():
    class Params:
        transactionId = faker.random_int()
        userId = faker.random_int()
        cardNumber = faker.word()
        transactionDate = faker.word()
        transactionAmount = faker.random_int()
        deviceId = faker.word()
        merchantId = faker.random_int()

    return Params()

def test_should_raise_invalid_amount_if_negative_value_on_transaction_amount():
    request = make_sut_request()
    request.transactionAmount = -100
    with pytest.raises(InvalidAmountErrorException):
        CheckTransactionUsecase(make_sut_machine_learning_approve(), make_sut_transaction_repository(), make_sut_model_repository()).execute(request)

def test_should_return_sucess_if_correct_values_informed():
    request = make_sut_request()
    request.transactionAmount = 100
    response = CheckTransactionUsecase(make_sut_machine_learning_approve(), make_sut_transaction_repository(), make_sut_model_repository()).execute(request)    
    TestCase().assertEqual(response['recommendation'], APPROVE_TRANSACTION)

def test_should_return_deny_if_correct_values_informed():
    request = make_sut_request()
    request.transactionAmount = 100
    response = CheckTransactionUsecase(make_sut_machine_learning_deny(), make_sut_transaction_repository(), make_sut_model_repository()).execute(request)    
    TestCase().assertEqual(response['recommendation'], DENY_TRANSACTION)
