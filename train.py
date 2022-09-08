# Файл для обучения

import re   # библиотека регулярных выражений

input_dir = input("Здравствуйте, укажите директорию файла, с которого будут считаны данные."
                  "\n(Пример директории: C:\\Users\\myPC\\Desktop\\My_text.txt):")


def cleaned_text(file):     # Функция привидения текста в токены

    # Очищаем текст от лишних символов
    cleaned_file = re.sub("[^А-яа-я]", " ", file)

    # Привели токены в порядок путем привидения текста к нижнему регистру и разделением текста с помощью метода split()
    cleaned_file = cleaned_file.lower().split()
    return print(cleaned_file)


try:

    # Считываем текст с файла в директории
    f = open(input_dir, "r", encoding="utf-8")
    file = f.read()
    f.close()


except FileNotFoundError:   # Считываем текст, введённый вручную
    file = input(f"Файла в директории \"{input_dir}\" нет. Введите текст вручную:")

cleaned_text(file)