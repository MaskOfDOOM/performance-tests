from pydantic import BaseModel, Field, ConfigDict, HttpUrl
from enum import StrEnum
from tools.fakers import fake


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
    url: HttpUrl
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
    Описание структуры ответа получения статистики по операциям.
    """
    summary: OperationsSummarySchema

class GetOperationReceiptResponseSchema(BaseModel):
    """
    Структура ответа на запрос чека по операции по operation_id
    """
    receipt: OperationReceiptSchema

class GetOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа получения операции.
    """
    operation: OperationSchema

class MakeOperationRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    """
    Общие поля запроса для POST-запросов на создание операций
    """
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции комиссии.
    """
    pass

class MakeFeeOperationResponseSchema(BaseModel):
    operation: OperationSchema

class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции комиссии.
    """
    pass

class MakeTopUpOperationResponseSchema(BaseModel):
    operation: OperationSchema

class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции комиссии.
    """
    pass

class MakeCashbackOperationResponseSchema(BaseModel):
    operation: OperationSchema

class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции комиссии.
    """
    pass

class MakeTransferOperationResponseSchema(BaseModel):
    operation: OperationSchema

class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции комиссии.
    """
    category: str = Field(default_factory=fake.category)

class MakePurchaseOperationResponseSchema(BaseModel):
    operation: OperationSchema
    

class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции комиссии.
    """
    pass

class MakeBillPaymentOperationResponseSchema(BaseModel):
    operation: OperationSchema

class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции комиссии.
    """
    pass

class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    operation: OperationSchema
