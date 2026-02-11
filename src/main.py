class Product:
    def __init__(self, name, description, price, quantity):
        if price <= 0 or not isinstance(price, float):
            raise ValueError("Price must be a positive number.")
        if quantity < 0 or not isinstance(quantity, int):
            raise ValueError("Quantity must be a non-negative integer.")

        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, data):
        try:
            return cls(data["name"], data["description"], data["price"], data["quantity"])
        except KeyError as e:
            raise ValueError(f"Missing required field: {e.args[0]}") from None

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        elif value > 0:
            self._price = value
        else:
            print("Warning: Price set to zero.")
            self._price = 0


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += sum(p.quantity for p in products)

    def add_product(self, product):
        self.products.append(product)
        # Увеличим общую сумму товаров только на количество добавляемого продукта
        Category.product_count += product.quantity


# Тестирование
if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product({
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    })
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    try:
        new_product.price = -100
    except ValueError as err:
        print(err)

    new_product.price = 0
    print(new_product.price)

