class Product:
    """Класс описывает товар."""

    def __init__(self, name, description, price, quantity):
        self.__name = name
        self.__description = description
        self.__price = price
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Ошибка: цена не должна быть нулевой или отрицательной!")
        else:
            self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Количество товара не может быть отрицательным!")
        else:
            self.__quantity = value

    def __repr__(self):
        return f'Product({self.name}, {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.name}, {self.price:.2f} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Операция возможна только между объектами класса Product")

    @staticmethod
    def validate_price(price):
        try:
            price_value = float(price)
            if price_value <= 0:
                raise ValueError("Цена должна быть положительной")
            return True
        except (ValueError, TypeError):
            return False

    @classmethod
    def new_product(cls, data, existing_products=None):
        name = data['name']
        description = data.get('description', '')
        price = float(data['price'])
        quantity = int(data['quantity'])

        if existing_products is not None:
            for product in existing_products:
                if product.name == name:
                    product.quantity += quantity
                    if product.price < price:
                        product.price = price
                    return product

        return cls(name, description, price, quantity)


class Category:
    _counter = 0  # Статическая переменная для подсчета товаров

    def __init__(self, name, description="", products=None):
        self.__name = name
        self.__description = description
        if products is None:
            self.__products = []
        else:
            self.__products = products

    @property
    def name(self):
        return self.__name

    def product_count(self):
        return len(self.__products)

    def add_product(self, product):
        self.__products.append(product)
        Category._counter += 1

    @property
    def products(self):
        return self.__products

    def __repr__(self):
        return f'Category(\n{self.products}\n)'

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f'Категория "{self.name}", количество продуктов: {total_quantity} шт.'
