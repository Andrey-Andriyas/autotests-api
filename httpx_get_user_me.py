import httpx

# POST-запрос
login_payload = {
    "email": "mail@mail.ru",
    "password": "11111"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status Code: ", login_response.status_code)


# GET-запрос
access_token = login_response_data["token"]["accessToken"]

headers = {
    "Authorization": f"Bearer {access_token}"
}

get_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

get_response_data = get_response.json()

print("Get response:", get_response_data)
print("Status Code:", get_response.status_code)