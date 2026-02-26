import pytest
from src.models import Product, Smartphone, LawnGrass, Category


@pytest.fixture
def base_product():
    return Product("Test Product", "This is a test product.", 100.0, 10)


@pytest.fixture
def smartphone():
    return Smartphone(
        "Galaxy",
        "A great phone",
        "Model-X",
        128,
        "Black",
        90.0,
        500.0,
        5
    )


@pytest.fixture
def lawn_grass():
    return LawnGrass(
        "Green Grass",
        "Best for lawns",
        "Russia",
        "10 дней",
        "Green",
        10.0,
        20
    )


@pytest.fixture
def category():
    return Category("Electronics", "All kinds of electronics here")


def test_base_product_repr(base_product):
    assert repr(base_product) == "Product(Test Product, 100.0, 10)"


def test_smartphone_str(smartphone):
    assert str(smartphone) == "Galaxy: Model-X, 128 ГБ, Black"


def test_lawn_grass_str(lawn_grass):
    assert str(lawn_grass) == "Green Grass: Russia, 10 дней, Green"


def test_category_add_product(category, base_product):
    category.add_product(base_product)
    assert len(category.products) == 1
    assert category.product_count() == 1


def test_new_product_creation():
    product_data = {
        "name": "New Phone",
        "description": "",
        "price": "500.0",
        "quantity": "1"
    }
    result = Product.new_product(product_data)
    assert isinstance(result, Product)
    assert result.name == "New Phone"
    assert result.price == 500.0
    assert result.quantity == 1


def test_addition_of_same_type_objects():
    prod1 = Product("Phone A", "First phone", 100.0, 2)
    prod2 = Product("Phone B", "Second phone", 200.0, 3)
    with pytest.raises(NotImplementedError):
        prod1 + prod2


def test_invalid_addition_raises_error():
    prod1 = Product("Phone A", "First phone", 100.0, 2)
    with pytest.raises(NotImplementedError):
        prod1 + "Invalid object"


def test_setter_validations():
    prod = Product("Test Product", "Test Description", 100.0, 10)

    # Цена меньше нуля вызывает ошибку
    with pytest.raises(ValueError):
        prod.price = -50.0

    # Отрицательное количество товаров недопустимо
    with pytest.raises(ValueError):
        prod.quantity = -5

    # Нулевое количество также недопустимо
    with pytest.raises(ValueError):
        prod.quantity = 0


def test_category_static_fields():
    Category.category_count = 0  # Сбрасываем счётчик
    Category("Electronics")     # Просто создаём категорию, не сохраняем ссылку
    Category("Sports Goods")    # А вторая категория тоже просто создаётся
    assert Category.category_count == 2


def test_add_product_to_category_increases_counter():
    Category._counter = 0  # Обязательно обнулить счётчик перед началом теста!
    cat = Category("Books")
    book1 = Product("Book Title", "Some description", 100.0, 10)
    cat.add_product(book1)
    assert Category._counter == 1


def test_middle_price_with_products():
    cat = Category("Phones")
    phone1 = Product("Phone X", "Great quality", 500.0, 5)
    phone2 = Product("Phone Y", "High performance", 700.0, 3)
    cat.add_product(phone1)
    cat.add_product(phone2)
    avg_price = cat.middle_price()
    assert avg_price == 600.0


def test_middle_price_without_products():
    empty_cat = Category("Empty Category")
    avg_price = empty_cat.middle_price()
    assert avg_price == 0
