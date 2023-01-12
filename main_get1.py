import requests

response = requests.get("https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=%D0%AF%D0%BA%D1%83%D1%82%D1%81%D0%BA&format=json")

# print(response, type(response))

if response:
    print(response.content)
else:
    print("Ошибка выполнения запроса")
    print("http статус:", response.status_code, "(", response.reason, ")")
