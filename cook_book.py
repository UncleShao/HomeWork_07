import json

keys = ['ingridient_name', 'quantity', 'measure', ]
cook_book_dict = {}

with open('recipes.txt') as text:
    # только непустые линии
    lines = []
    for line in text:
        line = line.strip()
        if line:
            lines.append(line)
        continue
    lines = iter(lines)  # https://docs.python.org/3/library/functions.html#iter

    # далее выталкиваем текст из iter
    for name in lines:  # шаг_1 - вытолкнутая тут линия - всегда блюдо
        cook_book_dict[name] = []
        num = next(lines)  # шаг_2 - следующая за блюдом - всегда номер

        for _ in range(int(num)):  # шаг_3 - затем надо вытолкнуть из iter - num линий состава блюда
            sostav_line = next(lines)  # одна из линий состава
            ingrid = sostav_line.split(' | ')  # разбить на ингридиенты
            z = zip(keys, ingrid)  # сопоставить ключ - https://docs.python.org/3/library/functions.html#zip
            sostav_dict = {k: v for (k, v) in z}  # генератор словаря ингридиентов
            cook_book_dict[name].append(sostav_dict)
            continue

        # тк все линии не пустые, и мы вытолкнули все линии текущего юляда, следующая лиция опять будет - блюдо
        continue

print(json.dumps(cook_book_dict, indent=2, ensure_ascii=False))













