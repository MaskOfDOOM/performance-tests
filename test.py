from clients.grpc.gateway.operations.client import build_operations_gateway_grpc_client


def test_make_purchase_operation():
    # Создаем клиента gRPC
    client = build_operations_gateway_grpc_client()
    
    # Получаем данные для теста
    card_id = "642c0f59-3641-4386-81dd-3d0d9e0b3e3c"  # Используйте реальный card_id
    account_id = "b9ac6f3c-b3c1-44f5-8657-fdd9a64e999d"  # Используйте реальный account_id
    
    try:
        # Выполняем операцию
        response = client.make_purchase_operation(card_id=card_id, account_id=account_id)
        print("Операция покупки выполнена успешно:")
        print(response)
    except Exception as e:
        print(f"Ошибка при выполнении покупки: {e}")

# Вызов теста
test_make_purchase_operation()
