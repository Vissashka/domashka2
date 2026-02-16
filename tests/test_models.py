import pytest
from src.models import Product, Smartphone, LawnGrass, Category

@pytest.fixture
def sample_product():
    return Product("Sample Product", "Test Description", 1000, 10)

@pytest.fixture
def smartphone():
    return Smartphone("Galaxy S23", "Description", 180000, 5, 95.5, "S23", 256, "Silver")

@pytest.fixture
def lawn_grass():
    return LawnGrass("Elite Grass", "Premium seeds", 500, 20, "Germany", "10 days", "Green")

@pytest.fixture
def category():
    return Category("Electronics", "High-quality electronics", [])

def test_base_product_init(sample_product):
    assert sample_product.name == "Sample Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 1000
    assert sample_product.quantity == 10

def test_smartphone_properties(smartphone):
    assert smartphone.name == "Galaxy S23"
    assert smartphone.description == "Description"
    assert smartphone.price == 180000
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23"
    assert smartphone.memory == 256
    assert smartphone.color == "Silver"

def test_lawn_grass_properties(lawn_grass):
    assert lawn_grass.name == "Elite Grass"
    assert lawn_grass.description == "Premium seeds"
    assert lawn_grass.price == 500
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Germany"
    assert lawn_grass.germination_period == "10 days"
    assert lawn_grass.color == "Green"

def test_category_add_product(category, smartphone):
    category.add_product(smartphone)
    assert smartphone in category.products
    assert category.product_count() == 1

def test_category_remove_product(category, smartphone):
    category.add_product(smartphone)
    category.remove_product(smartphone)
    assert smartphone not in category.products
    assert category.product_count() == 0

def test_category_product_count(category, smartphone, lawn_grass):
    category.add_product(smartphone)
    category.add_product(lawn_grass)
    assert category.product_count() == 2

def test_category_raise_type_error_on_invalid_product(category):
    with pytest.raises(TypeError):
        category.add_product("Invalid object")

def test_category_string_representation(category, smartphone):
    category.add_product(smartphone)
    expected_output = f"Категория: Electronics, Описание: High-quality electronics, Продукты: 1"
    assert str(category) == expected_output
