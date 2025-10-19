import writer
import reader


def main():
    print("Запуск программы")
    print("Изменение как в person3")

    # Создаем текстовый файл
    writer.create_file()

    # Читаем и выводим содержимое
    reader.read_file()

    print("Программа завершена")


if __name__ == "__main__":
    main()