from abc import ABC, abstractmethod
from typing import Dict, Optional
from pydantic import BaseModel
from enum import Enum


class RecommendationEnum(str, Enum):
    APPROVE = 'approve'
    DENY = 'deny'
    SUSPECT = 'suspect'

class CheckTransactionRequest(BaseModel):
    transactionId: int
    userId: int
    cardNumber: str
    transactionDate: str
    transactionAmount: str
    deviceId: str
    merchantId: int

class CheckTransactionResponse(BaseModel):
    transactionId: Optional[int]
    recommendation: Optional[RecommendationEnum]
    error: Optional[str]
