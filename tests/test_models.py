import pytest
from src.models import Product, Category


@pytest.fixture
def sample_product():
    return Product('Телефон', 'Смартфон последнего поколения', 50_000, 10)


@pytest.fixture
def empty_category():
    return Category()


class TestProduct:
    def test_init(self, sample_product):
        assert isinstance(sample_product, Product)
        assert sample_product.name == 'Телефон'
        assert sample_product.description == 'Смартфон последнего поколения'
        assert sample_product.price == 50_000
        assert sample_product.quantity == 10

    def test_getters_and_setters(self, sample_product):
        with pytest.raises(ValueError):
            sample_product.price = -100
        with pytest.raises(ValueError):
            sample_product.quantity = -5

        sample_product.price = 60_000
        assert sample_product.price == 60_000

    def test_validate_price(self):
        assert Product.validate_price('100') == True
        assert Product.validate_price('-100') == False
        assert Product.validate_price('abc') == False

    def test_new_product_classmethod(self):
        product_data = {'name': 'Ноутбук', 'description': 'Игровой ноутбук', 'price': '80000', 'quantity': '5'}
        new_product = Product.new_product(product_data)
        assert isinstance(new_product, Product)
        assert new_product.name == 'Ноутбук'
        assert new_product.price == 80000
        assert new_product.quantity == 5

        updated_product = Product.new_product({
            'name': 'Ноутбук',
            'description': 'Игровой ноутбук',  # добавили back описание
            'price': '90000',
            'quantity': '3'
        }, [new_product])
        assert updated_product.quantity == 8
        assert updated_product.price == 90000


class TestCategory:
    def test_add_product(self, empty_category, sample_product):
        empty_category.add_product(sample_product)
        assert len(empty_category._Category__products) == 1
        assert empty_category.products == 'Телефон, 50000.00 руб. Остаток: 10 шт.'

    def test_counter_increase(self, empty_category, sample_product):
        initial_count = Category._counter
        empty_category.add_product(sample_product)
        assert Category._counter == initial_count + 1

    def test_repr(self, empty_category, sample_product):
        empty_category.add_product(sample_product)
        repr_str = str(empty_category).strip().replace('\n', '')
        expected_output = 'Category(Телефон, 50000.00 руб. Остаток: 10 шт.)'
        assert repr_str == expected_output

