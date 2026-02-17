from abc import ABCMeta, abstractmethod


class BaseProduct(metaclass=ABCMeta):
    """
    Абстрактный класс для общих свойств всех продуктов.
    """

    def __init__(self, name, description, price, quantity):
        self._name = name
        self._description = description
        self._price = price
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена должна быть больше нуля.")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Количество должно быть неотрицательным.")
        self._quantity = value

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class LoggingMixin:
    """
    Класc-миксин для вывода сообщений при создании экземпляров.
    """

    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        params = ', '.join(map(str, args)) + \
            ', '.join(kwargs.keys()) if kwargs else ''
        print(f"Создан объект {class_name}({params})")
        super().__init__(*args, **kwargs)


class Product(BaseProduct, LoggingMixin):
    """
    Общий класс товаров магазина.
    """

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', " \
               f"{self.price}, {self.quantity})"

    def __str__(self):
        return f"Товар: {self.name}. " \
               f"Цена: {self.price} руб., " \
               f"остаток: {self.quantity}"


class Smartphone(Product):
    """
    Конкретный класс смартфонов.
    """

    def __add__(self, other):
        if isinstance(other, Smartphone):
            return self.price + other.price  # Суммируем цены
        else:
            raise TypeError("Несовместимые типы для сложения")

    def __init__(
            self,
            name,
            description,
            price,
            quantity,
            efficiency,
            model,
            memory,
            color):
        super().__init__(name, description, price, quantity)
        self._efficiency = efficiency
        self._model = model
        self._memory = memory
        self._color = color

    @property
    def efficiency(self):
        return self._efficiency

    @property
    def model(self):
        return self._model

    @property
    def memory(self):
        return self._memory

    @property
    def color(self):
        return self._color

    def __repr__(self):
        return f"Smartphone('{self.name}', '{self.description}', " \
               f"{self.price}, {self.quantity}, {self.efficiency}, " \
               f"'{self.model}', {self.memory}, '{self.color}')"

    def __str__(self):
        return (
            f"Смартфон: {self.name},\n"
            f"Модель: {self.model},\n"
            f"Цвет: {self.color},\n"
            f"Эффективность: {self.efficiency}%"
        )


class LawnGrass(Product):
    """
    Конкретный класс газонной травы.
    """

    def __add__(self, other):
        if isinstance(other, LawnGrass):
            return self.price + other.price  # Сумма цен
        else:
            raise TypeError("Несовместимые типы для сложения")

    def __init__(
            self,
            name,
            description,
            price,
            quantity,
            country,
            germination_period,
            color):
        super().__init__(name, description, price, quantity)
        self._country = country
        self._germination_period = germination_period
        self._color = color

    @property
    def country(self):
        return self._country

    @property
    def germination_period(self):
        return self._germination_period

    @property
    def color(self):
        return self._color

    def __repr__(self):
        return (
            f"LawnGrass('"
            f"{self.name}', "
            f"'{self.description}', "
            f"{self.price}, "
            f"{self.quantity}, "
            f"'{self.country}', "
            f"'{self.germination_period}', "
            f"'{self.color}'"
            ")"
        )

    def __str__(self):
        return (
            f"Газонная трава: {self.name},\n"
            f"Страна происхождения: {self.country},\n"
            f"Период всхожести: {self.germination_period},\n"
            f"Цвет: {self.color}"
        )


class Category:
    categories = []

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        if products is None:
            self._products = []
            self.count = 0  # Начнём с нуля продуктов
        else:
            self._products = list(products)
            self.count = len(products)
        Category.categories.append(self)

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, value):
        if all(isinstance(item, Product) for item in value):
            self._products = value
            self.count = len(value)  # Сразу установим новое количество
        else:
            raise ValueError("Список продуктов должен содержать только " +
                             "объекты Product.")

    def product_count(self):
        """Возвращает количество продуктов в данной категории"""
        return self.count

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Тип объекта не подходит")
        if product not in self._products:
            self._products.append(product)
            self.count += 1  # Увеличили счётчик на единицу

    def remove_product(self, product):
        if product in self._products:
            self._products.remove(product)
            self.count -= 1  # Уменьшаем счётчик на единицу
        else:
            raise ValueError("Этот продукт отсутствует в категории")

    def __repr__(self):
        return f"Category({self.name}, {len(self._products)} продуктов)"

    def __str__(self):
        return (
            f"Категория: {self.name}\n"
            f"Описание: {self.description}\n"
            f"Продуктов: {len(self._products)}"
        )
