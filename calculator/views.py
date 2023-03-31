from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def recipe_info(request, _recipe):

    person = request.GET.get("servings", 1)
    name_recipe = _recipe
    _dict = {}

    for ingredient, amount in DATA[name_recipe].items():
        _dict[ingredient] = round((amount * int(person)), 2)
        DATA[name_recipe].update(_dict)
    name_recipe = _recipe
    context = {"recipe": DATA[name_recipe]}

    return render(request, template_name="calculator/index.html", context=context)

