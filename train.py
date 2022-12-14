# Файл для обучения

from gensim.models import Word2Vec as w2v
import numpy as np


def tokenizer():
    import re  # библиотека регулярных выражений

    answer = 1
    text = ''

    while answer != 2:
        try:
            answer = int(input("У вас есть данные, которые вы хотите считать? (1 - Да, 2 - Нет): "))

            if answer == 1:
                input_dir = input("Укажите директорию, в которых хранятся файлы."
                                  "\n(Пример директории: C:\\Users\\myPC\\Desktop\\My_text):")
                try:
                    # Считываем текст с файла в директории
                    f = open(input_dir, "r", encoding="utf-8")
                    file = f.read()
                    f.close()

                except FileNotFoundError:  # Пропускаем ошибку о том, что файл не найден
                    print(f"Файла \"{input_dir}\" нет.")
                    continue

                # for word in text:
                #     if len(word) > 1:
                text += file

            if (answer != 1) and (answer != 2):
                print("Введите \"1\" либо \"2\": ")
                continue

        except ValueError:
            print("Введите цифру!")

    tokenizer = re \
        .sub("[^А-яа-я]", " ", text) \
        .lower() \
        .split()


    # Записываем результат токенизации в файл
    f = open("data\\tokenizer.txt", "w", encoding="utf-8")
    f.write(str(tokenizer))
    f.close()

    return tokenizer


tokenizer = tokenizer()

# f = open("data\\tokenizer.txt", "r", encoding="utf-8")
# tokenizer =f.read()
# f.close()
# print(tokenizer)
# print(len(tokenizer))


# dict = {}
# for i in range(len(tokenizer)):
#     dict[i] = tokenizer[i]
# print(dict)

model = w2v(tokenizer, vector_size=150, window=10, min_count=2)
# model.train(tokenizer, total_examples=len(tokenizer), epochs=10)
model.save("model.model")
# vocab = model.wv.key_to_index
# print(vocab)

# sim_words = model.wv.most_similar("принц")
# print(sim_words)
