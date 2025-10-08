from clients.http.client import HTTPClient
from httpx import Response
from typing import TypedDict

class IssueVirtualCardRequestDict(TypedDict):
    """
    Структура данных для выпуска виртуальной карты.
    """
    userId: str
    accountId: str

class IssuePhysicalCardRequestDict(TypedDict):
    """
    Структура данных для выпуска физической карты.
    """
    userId: str
    accountId: str

class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway
    """
    def issue_virtual_card_api(self, request) -> Response:
        """
        Создание виртуальной карты

        :param request: Словарь с данными, необходимыми для выпуска карты
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)
    

    def issue_physical_card_api(self, request) -> Response:
        """
        Создание физической карты

        :param request: Словарь с данными, необходимыми для выпуска карты
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)