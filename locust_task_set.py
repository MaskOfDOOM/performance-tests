from locust import HttpUser, between, task, TaskSet, SequentialTaskSet

class CheckOutFlow(SequentialTaskSet):
    @task
    def open_cart(self):
        self.client.get("/cart")

    @task
    def checkout(self):
        self.client.get("/checkout")

    @task
    def confirm(self):
        self.client.get("/order/confirm")


class ShopUser(HttpUser):
    tasks = [CheckOutFlow]
    wait_time = between(1, 3)


    

    