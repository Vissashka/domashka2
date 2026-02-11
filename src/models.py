class Product:
    """Класс описывает товар."""

    def __init__(self, name, description, price, quantity):
        """
        Инициализация объекта товара.

        :param name: наименование товара
        :param description: описание товара
        :param price: цена товара
        :param quantity: количество товара
        """
        self.__name = name  # Приватный атрибут названия
        self.__description = description  # Приватный атрибут описания
        self.__price = price  # Приватный атрибут цены
        self.__quantity = quantity  # Приватный атрибут количества

    # Свойства для приватных атрибутов (геттеры и сеттеры)

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
        """
        Класс-метод создаёт новый продукт или увеличивает количество у существующего товара.

        :param data: словарь с параметрами товара
        :param existing_products: список существующих объектов Product
        :return: объект типа Product
        """
        name = data['name']
        description = data.get('description', '')
        price = float(data['price'])
        quantity = int(data['quantity'])

        if existing_products is not None:
            for product in existing_products:
                if product.name == name:
                    product.quantity += quantity  # Увеличение количества через сеттер
                    if product.price < price:
                        product.price = price  # Выбираем наибольшую цену
                    return product

        return cls(name, description, price, quantity)

    def __repr__(self):
        return f'Product({self.name}, {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.name}, {self.price:.2f} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Операция возможна только между объектами класса Product")



class Category:
    """Класс представляет собой категорию товаров."""

    _counter = 0  # Счётчик товаров

    def __init__(self):
        """
        Инициализирует категорию с пустым приватным списком товаров.
        """
        self.__products = []  # Приватный атрибут-список товаров

    def add_product(self, product):
        """
        Добавляет продукт в категорию и увеличивает счётчик товаров.

        :param product: объект класса Product
        """
        self.__products.append(product)
        Category._counter += 1  # Инкрементируем счётчик

    @property
    def products(self):
        """
        Возвращает строковое представление списка товаров категории.
        """
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price:.2f} руб. Остаток: {product.quantity} шт.")
        return "\n".join(result)

    def __repr__(self):
        return f'Category(\n{self.products}\n)'

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f'Категория "{self.__class__.__name__}", количество продуктов: {total_quantity} шт.'


