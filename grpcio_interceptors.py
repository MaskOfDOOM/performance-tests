import grpc
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.users.rpc_get_user_pb2 import GetUserRequest


class SimpleLoggingInterceptor(grpc.UnaryUnaryClientInterceptor):
    def intercept_unary_unary(self, continuation, client_call_details, request):
        print(client_call_details, type(client_call_details))
        print(f"Calling method: {client_call_details.method}")
        # return super().intercept_unary_unary(continuation, client_call_details, request)
        response = continuation(client_call_details, request)

        return response

channel = grpc.insecure_channel("localhost:9003")
intercept_channel = grpc.intercept_channel(channel, SimpleLoggingInterceptor())

stub = UsersGatewayServiceStub(intercept_channel)

request = GetUserRequest(id="02bed40e-6a3b-483c-bec6-9d2013941b02")
response = stub.GetUser(request)
print(response)