class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, letter):
        sorted_list = [item for item in self.products if item.startswith(letter)]
        return sorted_list

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        sorted_items = '\n'.join(sorted(self.products))
        result += sorted_items
        return result
