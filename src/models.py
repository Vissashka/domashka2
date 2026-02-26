import abc


class LoggingMixin:
    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        params = ', '.join(f'{k}={v}' for k, v in kwargs.items())
        print(
            f'Создан экземпляр {class_name}({params})',
            flush=True)  # Чёткое указание на stdout
        super().__init__(*args, **kwargs)


class BaseProduct(metaclass=abc.ABCMeta):
    """
    Абстрактный базовый класс для всех типов продукции.
    """

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
            raise ValueError(
                "Ошибка: цена не должна быть нулевой или отрицательной!")
        else:
            self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Количество товара не может быть отрицательным!")
        elif value == 0:
            raise ValueError(
                "Товар с нулевым количеством не может быть добавлен!")
        else:
            self.__quantity = value

    def __repr__(self):
        return f"Product({self.name}, {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}, " \
               f"{self.price:.2f} руб., " \
               f"Остаток: {self.quantity} шт."

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
        name = data["name"]
        description = data.get("description", "")
        price = float(data["price"])
        quantity = int(data["quantity"])

        if existing_products is not None:
            for product in existing_products:
                if product.name == name:
                    product.quantity += quantity
                    if product.price < price:
                        product.price = price
                    return product

        return cls(name, description, price, quantity)

    # Определяем метод __add__, который запрещает сложение любых объектов
    def __add__(self, other):
        raise NotImplementedError("Сложение объектов не поддерживается")


class Product(BaseProduct):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)


class Smartphone(Product):
    """Класс описывает смартфон."""

    def __init__(
            self,
            name,
            description,
            model,
            memory,
            color,
            efficiency,
            price,
            quantity):
        super().__init__(name, description, price, quantity)
        self.model = model
        self.memory = memory
        self.color = color
        self.efficiency = efficiency

    def __repr__(self):
        return (
            f'Smartphone({self.name}, '
            f'{self.model}, '
            f'{self.memory}, '
            f'{self.color})'
        )

    def __str__(self):
        return f'{self.name}: {self.model}, {self.memory} ГБ, {self.color}'


class LawnGrass(Product):
    def __init__(
            self,
            name,
            description,
            country,
            germination_period,
            color,
            price,
            quantity):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (
            f'{self.name}: '
            f'{self.country}, '
            f'{self.germination_period}, '
            f'{self.color}'
        )


class Category:
    _counter = 0
    category_count = 0

    def __init__(self, name, description="", products=None):
        self.__name = name
        self.__description = description
        if products is None:
            self.__products = []
        else:
            self.__products = products
        # Увеличиваем счетчик категорий при создании новой категории
        Category.category_count += 1

    @property
    def name(self):
        return self.__name

    def product_count(self):
        return len(self.__products)

    def middle_price(self):
        if not self.__products:
            return 0
        prices = [p.price for p in self.__products]
        return round(sum(prices) / len(prices), 2)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только продукты и их производные классы.")

        self.__products.append(product)
        # Увеличиваем общий счетчик товаров
        Category._counter += 1

    @property
    def products(self):
        return self.__products

    def __repr__(self):
        return f"Category(\n{self.products}\n)"

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f'Категория "{self.name}", ' \
               f'Количество продуктов: {total_quantity} шт.'
