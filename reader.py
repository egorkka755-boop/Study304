def read_file():
    try:
        with open("text_file.txt", "r", encoding="utf-8") as f:
            content = f.read()

        print("\nСодержимое файла:")
        print("─" * 30)
        print(content)
        print("─" * 30)

    except FileNotFoundError:
        print("Файл text_file.txt не найден")