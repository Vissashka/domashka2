from src.models import Category, Product

if __name__ == "__main__":
    try:
        product1 = Product(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            5
        )
        product2 = Product("iPhone 15", "512GB, Gray Space", 210000.0, 8)
        product3 = Product(
            "Xiaomi Redmi Note 11",
            "1024GB, Синий",
            31000.0,
            14
        )

        category1 = Category(
            "Смартфоны",
            "Смартфоны — не только связь, но и удобство жизни",
            [product1, product2, product3],
        )

        print(f"Категории перед добавлением новых товаров:\n{category1}")

        # Добавляем новый товар
        product4 = Product('55" QLED 4K TV', "Фоновая подсветка", 123000.0, 7)
        category1.add_product(product4)

        print("\nКатегории после добавления новых товаров:")
        print(category1)
        print(f"Количество товаров в категории: {category1.product_count()}")

        # Проверяем создание нового товара методом .new_product()
        new_product_data = {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }

        new_product = Product.new_product(new_product_data)
        print("\nНовый созданный объект товара:", new_product)

        # Изменение цены и проверка реакции на ошибку
        try:
            new_product.price = 800
            print(f"\nНовая цена: {new_product.price}")

            # Установка недопустимой цены
            new_product.price = -100
        except ValueError as e:
            print(e)

        # Обновление количества товара
        new_product.quantity -= 3
        print(f"\nИзмененное количество товара: {new_product.quantity}")

        # Тестируем статический метод проверки цены
        print(Product.validate_price(-1))  # Должно вернуть False
        print(Product.validate_price(100))  # Должно вернуть True

    except Exception as ex:
        print(f"Произошла ошибка: {ex}")
