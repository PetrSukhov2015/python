import requests

# Пример GET-запроса
url = "https://ivcs.hi-tech.org/api/rest/public/applications"
response = requests.get(url)

# Проверка статуса ответа
if response.status_code == 200:
    data = response.json()  # Парсим JSON-ответ
    print("Данные получены:", data)
else:
    print(f"Ошибка: {response.status_code}")