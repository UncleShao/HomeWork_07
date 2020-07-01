import json

keys = ['ingridient_name', 'quantity', 'measure', ]
cook_book_dict = {}

with open('recipes.txt', encoding='utf8') as text:
    lines = []
    for line in text:
        line = line.strip()
        if line:
            lines.append(line)
        continue
    lines = iter(lines)

    for name in lines:
        cook_book_dict[name] = []
        num = next(lines)

        for _ in range(int(num)):
            sostav_line = next(lines)
            ingrid = sostav_line.split(' | ')
            z = zip(keys, ingrid)
            sostav_dict = {k: v for (k, v) in z}
            cook_book_dict[name].append(sostav_dict)
            continue
        continue

print(json.dumps(cook_book_dict, indent=2, ensure_ascii=False))


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book_dict[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
    else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def get_cook_book_with_quantity():
    cook_book = {}
    with open('cook_book.txt', encoding='utf8') as f:
        while True:
            name = f.readline().strip()
            if not name:
                break
            count = int(f.readline().strip())
            cook_book[name] = []
            line = f.readline().strip()
            while line:
                ingredients = line.split(" | ")
                ingredients_dict = {"ingredient_name": ingredients[0],
                                    "quantity": int(ingredients[1]),
                                    "measure": ingredients[2]}
                cook_book[name].append(ingredients_dict)
                line = f.readline().strip()

    return cook_book


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    cook_book_dict = get_cook_book_with_quantity("cook_book.txt")
    shop_list = get_shop_list_by_dishes(cook_book_dict, person_count)
    print_shop_list(shop_list)


create_shop_list()










