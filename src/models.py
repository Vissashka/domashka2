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
        return f"Product({self.name}, {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}, {self.price:.2f} руб., Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError(f"Нельзя складывать товары разных типов ({type(self).__name__} и {type(other).__name__}).")

        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Операция доступна только для объектов класса Product")

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


class Smartphone(Product):
    """Класс описывает смартфон."""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.model = model
        self.memory = memory
        self.color = color
        self.efficiency = efficiency


    def __repr__(self):
        return f'Smartphone({self.name}, {self.model}, {self.memory}, {self.color})'

    def __str__(self):
        return f'{self.name}: {self.model}, {self.memory} ГБ, {self.color}'


def __str__(self):
    return f'{self.name}: {self.country}, {self.germination_period}, {self.color}'


class LawnGrass(Product):
    """Класс описывает газонную траву."""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


    def __repr__(self):
        return f"LawnGrass({self.name}, {self.country}, {self.germination_period}, {self.color})"

    def __str__(self):
        return f'{self.name}: {self.country}, {self.germination_period}, {self.color}'


class Category:
    def __init__(self, name, description="", products=None):
        self.name = name
        self.description = description
        if products is None:
            self.__products = []
        else:
            self.__products = list(products)

    @property
    def products(self):
        return self.__products[:]  # возвращаем защищенную копию

    @products.setter
    def products(self, value):
        if all(isinstance(item, Product) for item in value):
            self.__products = list(value)
        else:
            raise TypeError("Список продуктов должен содержать только объекты класса Product")

    @property
    def products(self):
        return self.__products[:]  # возвращаем защищенную копию

    @products.setter
    def products(self, value):
        if all(isinstance(item, Product) for item in value):
            self.__products = list(value)
        else:
            raise TypeError("Список продуктов должен содержать только объекты класса Product")

    def remove_product(self, product):
        if product in self.__products:
            self.__products.remove(product)
        else:
            raise ValueError("Данный продукт не найден в категории")

    def product_count(self):
        return len(self.__products)

    @property
    def products(self):
        return self.__products[:]  # Безопасная копия списка

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    def remove_product(self, product):
        if product in self.__products:
            self.__products.remove(product)

    def product_count(self):
        return len(self.__products)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    def product_count(self):
        return len(self.__products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product и его наследников.")
        self.__products.append(product)

    @property
    def products(self):
        return self.__products[:]  # Возвращаем копию списка для защиты внутреннего состояния

    def __repr__(self):
        return f"Category(\n{self.products}\n)"

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f'Категория "{self.name}", Количество продуктов: {total_quantity} шт.'