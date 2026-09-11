import json


def save_employee_data(data, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def load_employee_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
