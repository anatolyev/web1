import json

cats_dict = {
      "name": "Барсик",
      "age": 7,
      "toys": [
        "Мышка",
        "Прутик",
        "Бантик",
        "Свой хвост"
      ]
}

with open('cats_33.json', 'w') as cat_file:
    json.dump(cats_dict, cat_file, ensure_ascii=False, indent=4, sort_keys=True)
