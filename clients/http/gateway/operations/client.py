from clients.http.client import HTTPClient
from typing import TypedDict
from httpx import Response

from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """
    Описание операции
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str

class OperationReceiptDict(TypedDict):
    """
    Описание структуры чека
    """
    url: str
    document: str

class OperationsSummaryDict(TypedDict):
    """
    Структура детализации операции
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций пользователя.
    """
    accountId: str

class GetOperationsResponseDict(TypedDict):
    """
    Описание структуры ответа на запрос операций по accountId
    """
    operations: list[OperationDict]



class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения списка операций пользователя.
    """
    accountId: str

class GetOperationsSummaryResponseDict(TypedDict):
    """
    Структура ответа на запрос детализации операции
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float

class GetOperationReceiptResponseDict(TypedDict):
    """
    Структура ответа на запрос чека по операции по operation_id
    """
    url: str
    document: str

class GetOperationResponseDict(TypedDict):
    operation: list[OperationDict]

class MakeFeeOperationResponseDict(TypedDict):
    operation: list[OperationDict]

class MakeTopUpOperationResponseDict(TypedDict):
    operation: list[OperationDict]

class MakeCashbackOperationResponseDict(TypedDict):
    operation: list[OperationDict]

class MakeTransferOperationResponseDict(TypedDict):
    operation: list[OperationDict]

class MakePurchaseOperationResponseDict(TypedDict):
    operation: list[OperationDict]
    category: str

class MakeBillPaymentOperationResponseDict(TypedDict):
    operation: list[OperationDict]

class MakeCashWithdrawalOperationResponseDict(TypedDict):
    operation: list[OperationDict]


class BaseOperationRequestDict(TypedDict):
    """
    Общие поля запроса для POST-запросов на создание операций
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeFeeOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных для создания операции по списанию комиссии
    """
    pass

class MakeTopUpOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных для создания операции пополнения счета
    """
    pass

class MakeCashbackOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных для создания операции по начислению кэшбека
    """
    pass

class MakeTransferOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных для создания операции по переводу д/с
    """
    pass

class MakePurchaseOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных для создания операции покупки
    """
    category: str

class MakeBillPaymentOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных для создания операции оплаты по счету
    """
    pass

class MakeCashWithdrawalOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных для создания операции снятия наличных средств
    """
    pass    



class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return Ответ от сервера (объект httpx.Response)
        """
        return self.get(f"/api/v1/operations/{operation_id}")
    
    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return Ответ от сервера (объект httpx.Response)
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")
    
    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получение списка операций для определенного счета по accountId.

        :param query: Словарь с параметрами запроса
        :return Ответ от сервера (объект httpx.Response)
        """
        return self.get("/api/v1/operations", params=query)
    
    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Получение статистики по операциям для определенного счета по accountId.

        :param query: Словарь с параметрами запроса
        :return Ответ от сервера (объект httpx.Response)
        """
        return self.get("/api/v1/operations/operations-summary", params=query)
    
    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для проведения операции по списанию комиссии.

        :param request: Словарь с данными, необходимыми для выполнения операции.
        :return Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)
    
    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для проведения операции по пополнению счета.

        :param request: Словарь с данными, необходимыми для выполнения операции.
        :return Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)
    
    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для проведения операции по начислению кэшбека.

        :param request: Словарь с данными, необходимыми для выполнения операции.
        :return Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)
    
    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для проведения операции по переводу д/с.

        :param request: Словарь с данными, необходимыми для выполнения операции.
        :return Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)
    
    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для проведения операции по списанию комиссии.

        :param request: Словарь с данными, необходимыми для проведения операции покупки.
        :return Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)
    
    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для проведения операции оплаты по счету.

        :param request: Словарь с данными, необходимыми для выполнения операции.
        :return Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)
    
    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для проведения операции снятия наличных средств.

        :param request: Словарь с данными, необходимыми для выполнения операции.
        :return Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)
    
    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()
    
    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()
    
    def get_operation_receipt(self, account_id: str) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(account_id)
        return response.json()
    
    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()
    
    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
        status="COMPLETED",
        amount=55.77,
        cardId=card_id,
        accountId=account_id
    )
        response = self.make_fee_operation_api(request)
        return response.json()
    
    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
        status="COMPLETED",
        amount=55.77,
        cardId=card_id,
        accountId=account_id
    )
        response = self.make_top_up_operation_api(request)
        return response.json()
    
    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
        status="COMPLETED",
        amount=55.77,
        cardId=card_id,
        accountId=account_id
    )
        response = self.make_cashback_operation_api(request)
        return response.json()
    
    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
        status="COMPLETED",
        amount=55.77,
        cardId=card_id,
        accountId=account_id
    )
        response = self.make_transfer_operation_api(request)
        return response.json()
    
    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
        status="COMPLETED",
        amount=55.77,
        cardId=card_id,
        accountId=account_id,
        category="taxi"
    )
        response = self.make_purchase_operation_api(request)
        return response.json()
    
    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
        status="COMPLETED",
        amount=55.77,
        cardId=card_id,
        accountId=account_id
    )
        response = self.make_bill_payment_operation_api(request)
        return response.json()
    
    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
        status="COMPLETED",
        amount=55.77,
        cardId=card_id,
        accountId=account_id
    )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())   