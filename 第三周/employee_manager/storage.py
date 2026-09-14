import json

def save_employee(employees,file_path):
    with open(file_path,"w",encoding="utf-8")as file:
        json.dump(employees,file,ensure_ascii=False,indent=2)
def load_employee(file_path):
    try:
        with open(file_path,"r",encoding="utf-8")as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return[]
    
