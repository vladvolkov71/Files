import os


def dish(f1):  # Функция, создающая словарь с рецептом одного блюда
    dish_ = {}
    name = f1.readline().strip()
    si = int(f1.readline().strip())
    ing = []
    for _ in range(si):
        ing_sl = {}
        j = f1.readline().split("|")
        ing_sl.setdefault('ingredient_name', j[0].strip())
        ing_sl.setdefault('quantity', int(j[1].strip()))
        ing_sl.setdefault('measure', j[2].strip())
        ing.append(ing_sl)
    dish_.setdefault(name, ing)
    return dish_


def get_shop_list_by_dishes(dishes, person_count):  # Функция создающая список ингридиентов для приготовления обеда
    list_ing = {}
    for d in dishes:
        for p in c_b('recipies.txt')[d]:
            list_ing.setdefault(p.pop('ingredient_name'), p)
    for v in list_ing.values():
        v['quantity'] *= person_count
    print(list_ing)


def c_b(f_rec):  # Функция составляющая словарь с рецептами из переданного файла
    with open(f_rec, 'r', encoding='utf-8') as file:
        cook_book = {}
        k = file.readlines().count("\n")
        file.seek(0)
        for n in range(k + 1):
            cook_book.update(dish(file))
            _ = file.readline()
    return cook_book


# Печать словаря рецептов
print(c_b('recipies.txt'))

# Печать списка ингридиентов для обеда

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


def f_list(dir_):  # Функция определяющая файлы в каталоге и подсчитывающая количество строк в них
    f_ = {}
    for i in os.listdir(dir_):
        with open(dir_ + '\\' + i, 'r', encoding='utf-8') as f:
            f_.setdefault(i, len(f.readlines()))
    return f_


def f_res(dir_):  # Функция создающая результирующий файл 'result.txt' из задания
    f_sorted = [i[0] for i in sorted(f_list(dir_).items(), key=lambda item: item[1])]
    os.remove('result.txt')
    for i in f_sorted:
        with open('result.txt', 'a', encoding='utf-8') as output:
            with open(dir_ + '\\' + i, 'r', encoding='utf-8') as file1:
                cont = file1.readlines()
                print(f"{i}", file=output)
                print(f"{f_list(dir_)[i]}", file=output)
                output.writelines(cont)
                output.write("\n")


# Запуск создания 'result.txt' из файлов, в каталоге "f"
f_res('f')
