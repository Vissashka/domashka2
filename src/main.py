from src.models import Category, Product, Smartphone, LawnGrass

if __name__ == "__main__":
    try:
        # Создаем три смартфона
        smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "S23 Ultra", 256, "Серый", 95.5)
        smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, "15", 512, "Gray space", 98.2)
        smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, "Note 11", 1024, "Синий", 90.3)

        # Создаем два объекта газонной травы
        grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
        grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

        # Печать характеристик телефонов
        print(smartphone1.name)
        print(smartphone1.description)
        print(smartphone1.price)
        print(smartphone1.quantity)
        print(smartphone1.efficiency)
        print(smartphone1.model)
        print(smartphone1.memory)
        print(smartphone1.color)

        print(smartphone2.name)
        print(smartphone2.description)
        print(smartphone2.price)
        print(smartphone2.quantity)
        print(smartphone2.efficiency)
        print(smartphone2.model)
        print(smartphone2.memory)
        print(smartphone2.color)

        print(smartphone3.name)
        print(smartphone3.description)
        print(smartphone3.price)
        print(smartphone3.quantity)
        print(smartphone3.efficiency)
        print(smartphone3.model)
        print(smartphone3.memory)
        print(smartphone3.color)

        # Печать характеристик газонной травы
        print(grass1.name)
        print(grass1.description)
        print(grass1.price)
        print(grass1.quantity)
        print(grass1.country)
        print(grass1.germination_period)
        print(grass1.color)

        print(grass2.name)
        print(grass2.description)
        print(grass2.price)
        print(grass2.quantity)
        print(grass2.country)
        print(grass2.germination_period)
        print(grass2.color)

        # Сумма двух смартфонов
        smartphone_sum = smartphone1 + smartphone2
        print(smartphone_sum)

        # Сумма двух видов газонной травы
        grass_sum = grass1 + grass2
        print(grass_sum)

        # Попытка сложения разнотипных объектов
        try:
            invalid_sum = smartphone1 + grass1
        except TypeError:
            print("Возникла ошибка TypeError при попытке сложения")
        else:
            print("Не возникла ошибка TypeError при попытке сложения")

        # Создаем категории и добавляем продукцию
        category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
        category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

        # Добавляем третий телефон в категорию
        category_smartphones.add_product(smartphone3)

        # Проверка содержимого категории
        print(category_smartphones.products)

        # Проверка количества продуктов в категории
        print(category_smartphones.product_count())  # Тут фикс обращения к методу

        # Проверка невозможности добавления произвольного объекта
        try:
            category_smartphones.add_product("Not a product")
        except TypeError:
            print("Возникла ошибка TypeError при добавлении не продукта")
        else:
            print("Не возникла ошибка TypeError при добавлении не продукта")

    except Exception as ex:
        print(f"Произошла ошибка: {ex}")
