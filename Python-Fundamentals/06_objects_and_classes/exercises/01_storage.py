class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product):
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):
        return self.storage


storage = Storage(4)
storage.add_product("pedal")
print(storage.get_products())
