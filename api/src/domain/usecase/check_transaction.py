from abc import ABC, abstractmethod
from typing import Dict, Optional
from pydantic import BaseModel
from enum import Enum


class RecommendationEnum(str, Enum):
    APPROVE = 'approve'
    DENY = 'deny'
    SUSPECT = 'suspect'

class CheckTransactionRequest(BaseModel):
    transaction_id: int
    user_id: int
    card_number: str
    transaction_date: str
    transaction_amount: str
    device_id: str

class CheckTransactionResponse(BaseModel):
    transaction_id: int
    recommendation: RecommendationEnum
