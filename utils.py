import json

from src.models import Category, Product


def load_data_from_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for cat_data in data["categories"]:
        # Переводим продукты из словарей в объекты Product
        products = [Product(**prod) for prod in cat_data["products"]]

        # Создаем объект Category с названием, описанием и продуктом
        category = Category(
            name=cat_data["name"],
            description=cat_data["description"],
            products=products,
        )

        categories.append(category)

    return categories
