from locust import User, between, task
from clients.http.gateway.users.schema import CreateUserResponseSchema
from clients.http.gateway.accounts.schema import GetAccountsResponseSchema
from clients.http.gateway.locust import GatewayHTTPTaskSet
from tools.locust.user import LocustBaseUser


class GetAccountsTaskSet(GatewayHTTPTaskSet):
    create_user_response: CreateUserResponseSchema | None = None
    get_accounts_response: GetAccountsResponseSchema | None = None

    @task(2)
    def create_user(self):
        """
        Создаём нового пользователя и сохраняем результат для последующих шагов.
        """
        self.create_user_response = self.users_gateway_client.create_user()

    @task(2)
    def open_deposit_account(self):
        """
        Открываем депозитный счёт для созданного пользователя.
        Проверяем, что пользователь создан.
        """
        if not self.create_user_response:
            return
        
        self.open_deposit_account_response = self.accounts_gateway_client.open_deposit_account(
            user_id=self.create_user_response.user.id
    )
    @task(6)
    def get_accounts(self):
        """
        Получаем инфо об открытых счетах пользователя.
        Проверяем, что пользователь создан/депозитный счёт для него открыт.
        """
        if not self.create_user_response:
            return
        
        self.get_accounts_response = self.accounts_gateway_client.get_accounts(
            user_id=self.create_user_response.user.id
        )

class GetAccountsUser(LocustBaseUser):
    """
    Пользователь Locust, исполняющий последовательный сценарий получения документов.
    """
    tasks = [GetAccountsTaskSet]
