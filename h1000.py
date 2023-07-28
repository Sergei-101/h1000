# Напишите следующие функции:
# * Нахождение корней квадратного уравнения
# * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.


import random
import csv
import json


def gen_csv(number_of_strings: int = 100, file_name:str = 'generate.csv'):
    test_list = []
    for _ in range(1, number_of_strings):
        test_dict = {}
        test_dict["a"] = random.randint(1, 100)
        test_dict["b"] = random.randint(1, 100)
        test_dict["c"] = random.randint(1, 100)
        test_list.append(test_dict)

    with open(file_name, 'w', encoding='utf-8', newline="") as f:
        fieldnames = ["a", "b", "c"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(test_list)


def form_korn_decor(func):
    FILECSV:str = 'generate.csv'

    def wrapper():
        res = []
        with open(FILECSV, 'r') as file:
            reader = csv.reader(file)
            for i in reader:
                a, b, c = map(int, i)
                res = [func(a, b, c)]
                print(f"Уравнение: {a}x^2 + {b}x + {c} = 0")
                print("Результат", res)
                res.append({"Уравнение": f"{a}x^2 + {b}x + {c} = 0", "Результат": res})

            return res

    return wrapper


def save_json(func, filename: str = 'generate.json'):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(res, file, indent=4)
            return res

        return wrapper




@save_json
@form_korn_decor
def form_korn(*args):
    a, b, c, *other = args
    discr = b ** 2 - 4 * a * c
    root_1 = (-b + discr ** (0.5)) / (2 * a)
    root_2 = (-b - discr ** (0.5)) / (2 * a)
    return str(root_1), str(root_2)


gen_csv()
print(form_korn())
