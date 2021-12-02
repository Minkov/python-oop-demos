from project.baked_food.bread import Bread
from project.bakery import Bakery

b = Bakery('Pri Gosho')

b.add_food('Bread', 'Topal', 2)
b.add_food('Bread', 'Pitka', 2.5)
b.add_food('Cake', 'Hubava', 7)

b.add_drink('Tea', 'Angliiski', 0.3, 'brand 1')

b.add_drink('Water', 'Mineralna', 1.5, 'Burgaska')

[b.add_table('InsideTable', n, (n + 5) % 7 + 1) for n in range(21, 23)]
[b.add_table('OutsideTable', n, (n + 5) % 7 + 1) for n in range(51, 53)]

print(b.reserve_table(7))
print(b.order_food(22, 'Mineralna', 'Mineralna', 'Mineralna', 'Topal', 'Hubava'))
print(b.order_drink(22, 'Mineralna', 'Mineralna', 'Mineralna', 'Topal', 'Hubava'))
