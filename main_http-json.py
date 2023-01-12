import requests

geocoder_request = f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={input('Введите назование географического объекта: ')}&format=json"

# print(response, type(response))
response = requests.get(geocoder_request)
if response:
    json_response = response.json()

    # print(json_response)
    # import json
    # with open('temp.json', 'w', encoding="utf8") as temp_file:
    #     json.dump(json_response, temp_file, ensure_ascii=False)
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_adress = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    toponym_coordinates = toponym["Point"]["pos"]
    print(toponym_adress, "имеет координаты", toponym_coordinates)
else:
    print("Ошибка выполнения запроса")
    print("http статус:", response.status_code, "(", response.reason, ")")