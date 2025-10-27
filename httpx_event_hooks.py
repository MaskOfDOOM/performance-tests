from httpx import Client, Request, Response
from datetime import datetime


def log_request(request: Request):
    datetime.now()
    request.extensions['start_time'] = datetime.now()
    print(f"REQUEST: {request.method}")

def log_response(response: Response):
    duration = datetime.now() - response.request.extensions['start_time']
    print(f"RESPONSE: {response.status_code}, {duration}")

client = Client(
    base_url="http://localhost:8003",
    event_hooks={"request": [log_request], "response": [log_response]}
    )
response = client.get("/api/v1/users/35162940-f2e0-430d-9bf4-3ace9c11b56b")

print(response)
