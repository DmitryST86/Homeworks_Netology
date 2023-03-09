from pprint import pprint

with open('recipe.txt', encoding='utf-8') as file:
    cookbook = {}
    for line in file:
        dish = line.strip()
        dish_amount = int(file.readline())
        dish_list = []
        for _ in range(dish_amount):
            structure = file.readline().strip()
            ingredient, count, unit_measure = structure.split(' | ')
            dish_list.append(
                {'ingredient_name': ingredient,
                 'quantity': count,
                 'measure': unit_measure}
            )
        cookbook[dish] = dish_list
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_by_person_count = {}
    for one_dish in dishes:
        if one_dish in cookbook.keys():
            for ingredients in cookbook[one_dish]:
                if ingredients['ingredient_name'] not in ingredients_by_person_count:
                    new_quantity = person_count * int(ingredients['quantity'])
                    ingredients_by_person_count[ingredients['ingredient_name']] = {'measure': ingredients['measure'],
                                                                                   'quantity': new_quantity}
                else:
                    ingredients_by_person_count[ingredients['ingredient_name']]['quantity'] += person_count * int(
                        ingredients['quantity'])
        else:
            print(f'Блюда - {one_dish} в книге рецептов нет!')
    return ingredients_by_person_count


pprint(cookbook, sort_dicts=False)
print('////////////////////////////////////////////////////////////////////////////////////')
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Фахитос', 'Омлет'], 2), sort_dicts=False)
