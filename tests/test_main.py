import pytest
from src.main import Product, Category

# === Тесты для класса Product ===

def test_product_init_valid():
    """
    Тест успешного создания объекта Product с корректными аргументами.
    """
    product = Product("Galaxy S23", "Premium phone", 100000.0, 10)
    assert product.name == "Galaxy S23"
    assert product.description == "Premium phone"
    assert product.price == 100000.0
    assert product.quantity == 10

def test_product_init_invalid_price():
    """
    Тест исключения при попытке задать отрицательную цену.
    """
    with pytest.raises(ValueError, match="Price must be a positive number."):
        Product("Galaxy S23", "Premium phone", -100000.0, 10)

def test_product_init_invalid_quantity():
    """
    Тест исключения при попытке задать отрицательное количество.
    """
    with pytest.raises(ValueError, match="Quantity must be a non-negative integer."):
        Product("Galaxy S23", "Premium phone", 100000.0, -10)

def test_product_new_product():
    """
    Тест создания объекта Product через фабричный метод new_product().
    """
    data = {
        "name": "Galaxy S23",
        "description": "Premium phone",
        "price": 100000.0,
        "quantity": 10
    }
    product = Product.new_product(data)
    assert product.name == "Galaxy S23"
    assert product.description == "Premium phone"
    assert product.price == 100000.0
    assert product.quantity == 10

def test_product_getter_and_setter():
    """
    Тест геттера и сеттера цены.
    """
    product = Product("Galaxy S23", "Premium phone", 100000.0, 10)
    product.price = 200000.0
    assert product.price == 200000.0

    # Тест попытки присвоить отрицательную цену
    with pytest.raises(ValueError, match="Price cannot be negative."):
        product.price = -100000.0

    # Тест предупреждения при присвоении нулевой цены
    product.price = 0
    assert product.price == 0

# === Тесты для класса Category ===

def test_category_init():
    """
    Тест инициализации объекта Category.
    """
    category = Category("Телефоны", "Различные телефоны", [])
    assert category.name == "Телефоны"
    assert category.description == "Различные телефоны"
    assert category.products == []

def test_category_with_initial_products():
    """
    Тест создания объекта Category с начальными продуктами.
    """
    product1 = Product("Galaxy S23", "Premium phone", 100000.0, 10)
    product2 = Product("iPhone 15", "New generation", 150000.0, 5)
    category = Category("Телефоны", "Различные телефоны", [product1, product2])
    assert len(category.products) == 2
    assert category.product_count == 15

def test_category_add_product():
    """
    Тест добавления продукта в категорию.
    """
    product1 = Product("Galaxy S23", "Premium phone", 100000.0, 10)
    category = Category("Телефоны", "Различные телефоны", [product1])
    product2 = Product("iPhone 15", "New generation", 150000.0, 5)
    category.add_product(product2)
    assert len(category.products) == 2
    assert category.product_count == 30

