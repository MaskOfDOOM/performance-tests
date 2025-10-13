from pydantic import BaseModel


class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = False

user = User(
    id="47", 
    name="Alice Smith", 
    email="alice@example.com",
    address=Address(city="New York", zip_code="10001")
)
print(user)