from project.drink import Drink
from project.food import Food
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for repo_product in self.products:
            if repo_product.name == product_name:
                return repo_product

    def remove(self, product_name):
        for repo_product in self.products:
            if repo_product.name == product_name:
                self.products.remove(repo_product)

    def __repr__(self):
        result = []
        for current_product in self.products:
            result.append(f"{current_product.name}: {current_product.quantity}")
        return '\n'.join(result)
