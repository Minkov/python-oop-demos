class Shop:
    _small_shop_capacity = 10

    def __init__(self, name, shop_type, capacity):
        self.name = name
        self.type = shop_type
        self.capacity = capacity
        self.items_count = 0
        self.items = {}

    @classmethod
    def small_shop(cls, name, shop_type):
        return cls(name, shop_type, cls._small_shop_capacity)

    # @staticmethod
    # def _can_add_item(items_count, capacity):
    #     return items_count < capacity - 1

    def _can_add_item(self):
        return self.items_count < self.capacity - 1

    def _can_remove_amount_of_item(self, item, amount):
        return item in self.items \
               and amount <= self.items[item]

    def add_item(self, item):
        # if not self._can_add_item(self.items_count, self.capacity):
        if not self._can_add_item():
            return 'Not enough capacity in the shop'
        if item not in self.items:
            self.items[item] = 0
        self.items[item] += 1
        self.items_count += 1
        return f'{item} added to the shop'

    def remove_item(self, item, amount):
        if not self._can_remove_amount_of_item(item, amount):
            return f'Cannot remove {amount} {item}'
        self.items[item] -= amount
        self.items_count -= amount
        return f'{amount} {item} removed from the shop'

    def __str__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
