from pydantic import BaseModel, Field, ConfigDict
from enum import StrEnum


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"

class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """
    Описание операции
    """
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class OperationReceiptSchema(BaseModel):
    """
    Описание структуры чека
    """
    url: str
    document: str

class OperationsSummarySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    """
    Структура детализации операции
    """
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class GetOperationsQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    """
    Структура данных для получения списка операций пользователя.
    """
    account_id: str = Field(alias="accountId")

class GetOperationsResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос операций по accountId
    """
    operations: list[OperationSchema]



class GetOperationsSummaryQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    """
    Структура данных для получения списка операций пользователя.
    """
    account_id: str = Field(alias="accountId")

class GetOperationsSummaryResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    """
    Структура ответа на запрос детализации операции
    """
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")

class GetOperationReceiptResponseSchema(BaseModel):
    """
    Структура ответа на запрос чека по операции по operation_id
    """
    url: str
    document: str

class GetOperationResponseSchema(BaseModel):
    operation: OperationSchema

class MakeFeeOperationResponseSchema(BaseModel):
    operation: OperationSchema

class MakeTopUpOperationResponseSchema(BaseModel):
    operation: OperationSchema

class MakeCashbackOperationResponseSchema(BaseModel):
    operation: OperationSchema

class MakeTransferOperationResponseSchema(BaseModel):
    operation: OperationSchema

class MakePurchaseOperationResponseSchema(BaseModel):
    operation: OperationSchema
    category: str

class MakeBillPaymentOperationResponseSchema(BaseModel):
    operation: OperationSchema

class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    operation: OperationSchema


class BaseOperationRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    """
    Общие поля запроса для POST-запросов на создание операций
    """
    status: str
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")