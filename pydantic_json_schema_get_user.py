from clients.users.public_users_client import get_public_users_client
from clients.users.private_users_client import get_private_users_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

# 1. Создаем публичного клиента и создаём пользователя
public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

create_user_response = public_users_client.create_user_api(create_user_request)
user_id = create_user_response.json()["user"]["id"]

# 2. Авторизуемся под созданным пользователем
auth_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(auth_user)

# 3. Получаем данные пользователя через API (возвращается Response)
get_user_response = private_users_client.get_user_api(user_id)

# 4. Генерируем JSON-схему из модели ответа
get_user_response_schema = GetUserResponseSchema.model_json_schema()

# 5. Валидируем JSON-ответ от API
validate_json_schema(
    instance=get_user_response.json(),
    schema=get_user_response_schema
)

print("Ответ GET /api/v1/users/{user_id} соответствует JSON-схеме.")