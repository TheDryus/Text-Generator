# Файл для обучения

import re   # библеотека регулярных выражений

input_dir = input("Здравствуйте, укажите директорию файла, с которого будут считаны данные."
                  "\n(Пример директории: C:\\Users\\andza\\Desktop\\My_text.txt):")


def cleaned_text(file):     # Функция привидения текста в токены

    # Очищаем текст от лишних символов
    cleaned_file = re.sub("[^А-яа-я]", " ", file)

    # Привели токены в порядок путем привидения текста к нижнему регистру и разделением текста с помощью метода split()
    cleaned_file = cleaned_file.lower().split()
    return print(cleaned_file)


try:

    # Считываем текст с файла в директории
    f = open(input_dir, "r", encoding="utf-8")
    # C:\Users\andza\AAA\GitHub\Text-Generator\Example_text.txt
    # f = open("Example_text.txt", "r", encoding="utf-8")
    file = f.read()
    f.close()
    cleaned_text(file)

except FileNotFoundError:   # Считываем текст, введённый вручную
    file = input(f"Файла в директории \"{input_dir}\" нет. Введите текст вручную:")
    cleaned_text(file)