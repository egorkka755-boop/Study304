

def create_file():
    text = """Привет! Это текстовый файл"""

    with open("text_file.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("Файл text_file.txt создан")