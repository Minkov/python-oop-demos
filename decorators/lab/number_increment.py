def number_increment(numbers):
    def increase():
        return [x + 1 for x in numbers]  # `numbers` is part of **closure**

    return increase()


print(number_increment([1, 2, 3]))  # 2, 3, 4
