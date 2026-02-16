import pytest
from src.models import Product, Smartphone, LawnGrass, Category

@pytest.fixture
def smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )

@pytest.fixture
def another_smartphone():
    return Smartphone(
        "iPhone 15 Pro Max",
        "1TB, Black Matte",
        220000.0,
        3,
        98.2,
        "Pro Max",
        1024,
        "Black Matte"
    )

@pytest.fixture
def lawn_grass():
    return LawnGrass(
        "Газонная трава",
        "Элитная смесь семян",
        500.0,
        20,
        "Германия",
        "10 дней",
        "Зелёный"
    )

@pytest.fixture
def category():
    return Category("Смартфоны", "Высокая производительность", [])

# Основные тесты для класса Product и его подклассов

def test_product_repr_and_str(smartphone):
    expected_repr = f'Smartphone(Samsung Galaxy S23 Ultra, S23 Ultra, 256, Серый)'
    expected_str = "Samsung Galaxy S23 Ultra: S23 Ultra, 256 ГБ, Серый"
    assert repr(smartphone) == expected_repr
    assert str(smartphone) == expected_str

def test_product_change_price(smartphone):
    original_price = smartphone.price
    smartphone.price = 200000.0
    assert smartphone.price == 200000.0
    smartphone.price = original_price  # Вернём обратно первоначальную цену

def test_product_negative_price(smartphone):
    with pytest.raises(ValueError):
        smartphone.price = -100.0

def test_product_change_quantity(smartphone):
    smartphone.quantity = 10
    assert smartphone.quantity == 10

def test_product_negative_quantity(smartphone):
    with pytest.raises(ValueError):
        smartphone.quantity = -5

# Тесты для категории

def test_category_product_count(category, smartphone):
    assert category.product_count() == 0  # Изначально пустой список
    category.add_product(smartphone)
    assert category.product_count() == 1  # После добавления одного продукта

def test_category_add_valid_product(category, smartphone):
    category.add_product(smartphone)
    assert smartphone in category.products

def test_category_add_invalid_product(category):
    with pytest.raises(TypeError):
        category.add_product("Некорректный продукт")

def test_category_add_multiple_products(category, smartphone, another_smartphone):
    category.add_product(smartphone)
    category.add_product(another_smartphone)
    assert len(category.products) == 2

# Тесты для метода validate_price

def test_validate_positive_price():
    assert Product.validate_price("100") == True

def test_validate_zero_price():
    assert Product.validate_price("0") == False

def test_validate_negative_price():
    assert Product.validate_price("-50") == False

def test_validate_non_numeric_price():
    assert Product.validate_price("abc") == False

# Дополнительные тесты для класса Smartphone

def test_smartphone_repr_and_str(smartphone):
    expected_repr = f'Smartphone(Samsung Galaxy S23 Ultra, S23 Ultra, 256, Серый)'
    expected_str = "Samsung Galaxy S23 Ultra: S23 Ultra, 256 ГБ, Серый"
    assert repr(smartphone) == expected_repr
    assert str(smartphone) == expected_str

# Тесты для LawnGrass

def test_lawn_grass_repr_and_str(lawn_grass):
    expected_repr = f"LawnGrass(Газонная трава, Германия, 10 дней, Зелёный)"
    expected_str = "Газонная трава: Германия, 10 дней, Зелёный"
    assert repr(lawn_grass) == expected_repr
    assert str(lawn_grass) == expected_str

# Тесты на исключение для суммы продуктов разного типа

def test_incompatible_product_sum(smartphone, lawn_grass):
    with pytest.raises(TypeError):
        result = smartphone + lawn_grass

# Тесты на суммирование стоимости однотипных продуктов

def test_product_sum(smartphone, another_smartphone):
    result = smartphone + another_smartphone
    expected = smartphone.price * smartphone.quantity + another_smartphone.price * another_smartphone.quantity
    assert result == expected

# Тест на суммарное количество продукции в категории

def test_category_total_products(category, smartphone, another_smartphone):
    category.add_product(smartphone)
    category.add_product(another_smartphone)
    total_qty = sum([p.quantity for p in category.products])
    assert total_qty == smartphone.quantity + another_smartphone.quantity

@pytest.mark.parametrize("invalid_product", ["Некорректный продукт", 123, {"key": "value"}])
def test_category_add_invalid_product(category, invalid_product):
    with pytest.raises(TypeError):
        category.add_product(invalid_product)

def test_category_remove_existing_product(category, smartphone):
    category.add_product(smartphone)
    category.remove_product(smartphone)
    assert smartphone not in category.products

def test_category_empty_products_list():
    empty_category = Category("Empty Category")
    assert empty_category.product_count() == 0

def test_category_total_products_with_one_product(category, smartphone):
    category.add_product(smartphone)
    assert category.product_count() == 1

def test_category_getting_all_products(category, smartphone, another_smartphone):
    category.add_product(smartphone)
    category.add_product(another_smartphone)
    retrieved_products = category.products
    assert smartphone in retrieved_products and another_smartphone in retrieved_products

def test_category_getting_products_copy(category, smartphone):
    category.add_product(smartphone)
    retrieved_products = category.products
    retrieved_products.pop()
    assert len(category.products) > 0

def test_category_description_is_optional():
    cat = Category("Без описания")
    assert cat.description == ''  # описание по умолчанию пустое
