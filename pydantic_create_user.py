from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    """
    Модель данных пользователя.

    Описывает структуру объекта пользователя, возвращаемого API.
    Используется как вложенный объект в ответах.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Модель запроса на создание пользователя.

    Содержит поля, необходимые для регистрации нового пользователя.
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Модель ответа на успешное создание пользователя.

    Содержит вложенный объект пользователя.
    """
    user: UserSchema



