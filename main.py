from pprint import pprint
import os
import time
with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        namedish = i.strip()
        countdish = int(file.readline())
        recipes = []
        cook_book[namedish] = recipes
        for ii in range(countdish):
            recipe = file.readline().strip()
            ing, title, unit = recipe.split(' | ')
            recipes.append({
                'ingredient_name': ing,
                'quantity': title,
                'measure': unit
            })
        file.readline()
    print(cook_book)

def get_shop_list_by_dishes(dishes, persons):
    shopping_list = {}
    for dish in dishes:
        for item in (cook_book[dish]):
            items = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity']) * persons})])
            if shopping_list.get(item['ingredient_name']):

                extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                              int(items[item['ingredient_name']]['quantity']))
                # print(extra_item)
                shopping_list[item['ingredient_name']]['quantity'] = extra_item
            else:
                shopping_list.update(items)
    print(f"Для приготовления блюд на {persons} человек  нам необходимо купить:")
    pprint(shopping_list)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

def rewrite_file(path1=None, path2=None, path3=None):
    if path1 or path2 or path3 is None:
        path1 = '1.txt'
        path2 = '2.txt'
        path3 = '3.txt'
        os.chdir('task2')
        outout_file = "rewrite_file.txt"
        file1_path = os.path.join(os.getcwd(), path1)
        file2_path = os.path.join(os.getcwd(), path2)
        file3_path = os.path.join(os.getcwd(), path3)
        with open(file1_path, 'r', encoding='utf-8') as f1:
            file1 = f1.readlines()
        with open(file2_path, 'r', encoding='utf-8') as f2:
            file2 = f2.readlines()
        with open(file3_path, 'r', encoding='utf-8') as f3:
            file3 = f3.readlines()
        with open(outout_file, 'w', encoding='utf-8') as f_total:

            if len(file1) < len(file2) and len(file1) < len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file2) < len(file1) and len(file2) < len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file3) < len(file1) and len(file3) < len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file1) > len(file2) and len(file1) > len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
            elif len(file2) > len(file1) and len(file2) > len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
            elif len(file3) > len(file1) and len(file3) > len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
    else:
        print('Давай лучше без параметров')
    return
rewrite_file()