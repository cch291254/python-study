with open("staff.txt","r",encoding="utf-8") as file:
    content=file.read()
print(content)

from pathlib import Path

file_path = Path("staff.txt")

if file_path.exists():
    content = file_path.read_text(encoding="utf-8")
    print(content)