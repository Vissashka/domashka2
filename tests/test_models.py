import pytest
from src.models import Product, Category

# Тестируем класс Product
def test_product_init():
    product = Product("Телефон", "Смартфон премиум-класса", 79999.99, 10)
    assert product.name == "Телефон"
    assert product.description == "Смартфон премиум-класса"
    assert product.price == 79999.99
    assert product.quantity == 10

def test_product_repr():
    product = Product("Телефон", "Смартфон премиум-класса", 79999.99, 10)
    expected_repr = 'Product(Телефон, 79999.99, 10)'
    assert repr(product) == expected_repr

def test_product_str():
    product = Product("Телефон", "Смартфон премиум-класса", 79999.99, 10)
    expected_str = 'Телефон, 79999.99 руб. Остаток: 10 шт.'
    assert str(product) == expected_str

def test_product_addition():
    product1 = Product("Телефон", "", 79999.99, 10)
    product2 = Product("Ноутбук", "", 159999.99, 5)
    total_cost = product1 + product2
    assert total_cost == 1599999.85

def test_invalid_price_setter():
    product = Product("Телефон", "Смартфон премиум-класса", 79999.99, 10)
    with pytest.raises(ValueError):
        product.price = -100

def test_invalid_quantity_setter():
    product = Product("Телефон", "Смартфон премиум-класса", 79999.99, 10)
    with pytest.raises(ValueError):
        product.quantity = -5

def test_validate_price_valid():
    valid_price = 100
    assert Product.validate_price(valid_price) == True

def test_validate_price_invalid():
    invalid_price = "-100"
    assert Product.validate_price(invalid_price) == False

def test_new_product():
    data = {
        'name': 'Новый телефон',
        'description': 'Новейшая модель телефона',
        'price': '100000',
        'quantity': '15'
    }
    product = Product.new_product(data)
    assert product.name == 'Новый телефон'
    assert product.description == 'Новейшая модель телефона'
    assert product.price == 100000
    assert product.quantity == 15

def test_new_product_existing_product():
    existing_products = [
        Product("Телефоны", "Телефоны бренда X", 50000, 10),
        Product("Ноутбуки", "Ноутбуки марки Y", 100000, 5)
    ]
    data = {'name': 'Телефоны', 'price': '60000', 'quantity': '5'}
    updated_product = Product.new_product(data, existing_products=existing_products)
    assert updated_product.quantity == 15
    assert updated_product.price == 60000

# Тестируем класс Category
def test_category_init_and_add_product():
    category = Category()
    product = Product("Планшет", "Планшет среднего уровня", 39999.99, 20)
    category.add_product(product)
    assert len(category.products.split("\n")) == 1
    assert "Планшет" in category.products

def test_category_repr():
    category = Category()
    product = Product("Планшет", "Планшет среднего уровня", 39999.99, 20)
    category.add_product(product)
    expected_repr = f'Category(\nПланшет, 39999.99 руб. Остаток: 20 шт.\n)'
    assert repr(category) == expected_repr

def test_category_str():
    category = Category()
    product = Product("Планшет", "Планшет среднего уровня", 39999.99, 20)
    category.add_product(product)
    expected_str = f'Категория "Category", количество продуктов: 20 шт.'
    assert str(category) == expected_str

