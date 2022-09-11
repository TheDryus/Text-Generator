# Файл для обучения

def tokenizer():
    import re  # библиотека регулярных выражений

    answer = 1
    text = ''
    while answer != 2:
        try:
            answer = int(input("У вас есть данные, которые вы хотите считать? (1 - Да, 2 - Нет): "))

            if answer == 1:
                input_dir = input("Здравствуйте, укажите директорию, в которых хранятся файлы."
                                  "\n(Пример директории: C:\\Users\\myPC\\Desktop\\My_text):")
                try:
                    # Считываем текст с файла в директории
                    f = open(input_dir, "r", encoding="utf-8")
                    file = f.read()
                    f.close()

                except FileNotFoundError:  # Пропускаем ошибку о том, что файл не найден
                    print(f"Файла \"{input_dir}\" нет.")
                    continue
                text += file

            if (answer != 1) and (answer != 2):
                print("Введите \"1\" либо \"2\": ")
                continue


        except ValueError:
            print("Введите цифру!")

    tokenizer = re. \
        sub("[^А-яа-я]", " ", text) \
        .lower() \
        .split(" ")

    for whitespace in tokenizer:
        if len(whitespace) == 0:
            tokenizer.remove(whitespace)

    tokenizer.pop()
    return tokenizer


tokenizer = tokenizer()

print(tokenizer)
f = open("tokenizer.txt", "w", encoding="utf-8")
f.write(str(tokenizer))
f.close()
# model = w2v(
#     tokenizer.tokenizer,
#     min_count=5,
#     epochs=100,
#     vector_size=100
# )
#
# model = model.wv.most_similar(["принц"], topn=5)
# print(model)
