from pydantic import BaseModel, Field, ConfigDict, HttpUrl, EmailStr ,ValidationError
from pydantic.alias_generators import to_camel
import uuid


class UserSchema(BaseModel):
    """
    Модель данных пользователя
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr = Field(default="johndoe@example.com")
    last_name: str = Field(alias="lastName", default="Doe")
    first_name: str = Field(alias="firstName", default="John")
    middle_name: str = Field(alias="middleName", default="Olegovich")
    phone_number: str = Field(alias="phoneNumber", default="88005553535")

user_default_model = UserSchema(
    id="84226095-6a24-4e45-9e83-383a477f9fe4",
    email="johndoe@example.com",
    lastName="Doe",
    firstName="John",
    middleName="Olegovich",
    phoneNumber="88005553535"
)
# print('User default model:', user_default_model)


class CreateUserRequestSchema(BaseModel):
    """
    Модель данных для запроса на создание пользователя
    """
    email: EmailStr = Field(default="johndoe@example.com")
    last_name: str = Field(alias="lastName", default="Doe")
    first_name: str = Field(alias="firstName", default="John")
    middle_name: str = Field(alias="middleName", default="Olegovich")
    phone_number: str = Field(alias="phoneNumber", default="88005553535")

create_user_request_model = CreateUserRequestSchema(
    email="johndoe@example.com",
    lastName="Doe",
    firstName="John",
    middleName="Olegovich",
    phoneNumber="88005553535"
)
# print('Create user request model:', create_user_request_model)



class CreateUserResponseSchema(BaseModel):
    """
    Модель данных ответа на запрос создания пользователя
    """
    user: UserSchema

create_user_response_model = CreateUserResponseSchema(
    user=user_default_model
)
# print('Create user response', create_user_response_model)