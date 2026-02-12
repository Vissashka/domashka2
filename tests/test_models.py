import pytest
from src.models import Product, Category


# --- Тесты для класса Product ---

def test_product_initialization():
    """Проверка правильного создания экземпляра Product"""
    product = Product("Test Phone", "Some description", 10000.0, 5)
    assert product.name == "Test Phone"
    assert product.description == "Some description"
    assert product.price == 10000.0
    assert product.quantity == 5


def test_product_price_setter_positive():
    """Проверка корректного задания цены"""
    product = Product("Test Phone", "Some description", 10000.0, 5)
    product.price = 15000.0
    assert product.price == 15000.0


def test_product_price_setter_negative():
    """Проверка защиты от неверной цены (отрицательная)"""
    product = Product("Test Phone", "Some description", 10000.0, 5)
    with pytest.raises(ValueError):
        product.price = -100


def test_product_quantity_setter_positive():
    """Проверка корректного задания количества"""
    product = Product("Test Phone", "Some description", 10000.0, 5)
    product.quantity = 10
    assert product.quantity == 10


def test_product_quantity_setter_negative():
    """Проверка защиты от неверного количества (отрицательное)"""
    product = Product("Test Phone", "Some description", 10000.0, 5)
    with pytest.raises(ValueError):
        product.quantity = -10


def test_validate_price():
    """Проверка статического метода для валидации цен"""
    valid_price = Product.validate_price(10000.0)
    invalid_price = Product.validate_price(-100)
    assert valid_price is True
    assert invalid_price is False


def test_new_product_class_method_existing():
    """Проверка class-метода при наличии товара"""
    product_data = {'name': 'Test Phone', 'description': '', 'price': 10000.0, 'quantity': 5}
    existing_products = [
        Product("Test Phone", "Some description", 5000.0, 3),
        Product("Another Phone", "Different description", 15000.0, 10)
    ]
    updated_product = Product.new_product(product_data, existing_products)
    assert updated_product.quantity == 8  # Старое кол-во плюс новое
    assert updated_product.price == 10000.0  # Максимальная цена выбрана


def test_new_product_class_method_new():
    """Проверка class-метода при отсутствии товара"""
    product_data = {'name': 'New Phone', 'description': '', 'price': 10000.0, 'quantity': 5}
    existing_products = [
        Product("Test Phone", "Some description", 5000.0, 3),
        Product("Another Phone", "Different description", 15000.0, 10)
    ]
    new_product = Product.new_product(product_data, existing_products)
    assert isinstance(new_product, Product)
    assert new_product.name == "New Phone"
    assert new_product.price == 10000.0
    assert new_product.quantity == 5


def test_product_representation():
    """Проверка метода __repr__"""
    product = Product("Test Phone", "Some description", 10000.0, 5)
    representation = repr(product)
    assert representation.startswith("Product(Test Phone")  # Ожидаемый вывод начинается с имени товара


def test_product_string_representation():
    """Проверка метода __str__"""
    product = Product("Test Phone", "Some description", 10000.0, 5)
    string_representation = str(product)
    assert "Test Phone" in string_representation
    assert "10000.00 руб." in string_representation
    assert "Остаток: 5 шт." in string_representation


def test_product_sum_operator():
    """Проверка операции суммирования двух продуктов"""
    product1 = Product("Test Phone", "Some description", 10000.0, 5)
    product2 = Product("Another Phone", "Other description", 15000.0, 10)
    total_cost = product1 + product2
    assert total_cost == 200000.0  # Общая стоимость всех товаров


# --- Тесты для класса Category ---

def test_category_initialization():
    """Проверка правильной инициализации категории"""
    category = Category("Electronics", "All kinds of electronics")
    assert category.products == [], "Список товаров должен быть пустым!"


def test_add_product_to_category():
    """Проверка добавления товара в категорию"""
    category = Category("Electronics", "All kinds of electronics")
    product = Product("Test Phone", "Some description", 10000.0, 5)
    category.add_product(product)
    assert category.product_count() == 1


def test_category_representation():
    """Проверка метода __repr__"""
    category = Category("Electronics", "All kinds of electronics")
    product = Product("Test Phone", "Some description", 10000.0, 5)
    category.add_product(product)
    representation = repr(category)
    expected_repr = f'Category(\n[Product(Test Phone, 10000.0, 5)]\n)'
    assert representation == expected_repr, "Представление не соответствует ожиданиям."


def test_category_string_representation():
    """Проверка метода __str__"""
    category = Category("Electronics", "All kinds of electronics")
    product = Product("Test Phone", "Some description", 10000.0, 5)
    category.add_product(product)
    string_representation = str(category)
    assert "Категория \"Electronics\"" in string_representation
    assert "количество продуктов: 5 шт." in string_representation


def test_get_total_quantity():
    """Проверка суммарного количества товаров в категории"""
    category = Category("Electronics", "All kinds of electronics")
    product1 = Product("Test Phone", "Some description", 10000.0, 5)
    product2 = Product("Another Phone", "Other description", 15000.0, 10)
    category.add_product(product1)
    category.add_product(product2)
    assert category.product_count() == 2
    assert sum([p.quantity for p in category.products]) == 15  # Суммарное количество товаров
