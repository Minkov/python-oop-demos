from project.fruit import Fruit

food = Fruit('Banana', '18/07/22')
print(food.expiration_date)
# print(food.expiration_date_as_date)

'''
lab: -> Mark as resources root
    food: -> Mark as sources root
        project:
            food.py
            fruit.py
    single_inheritance: -> Mark as sources root
        project:
            file1.py
            file2.py
'''