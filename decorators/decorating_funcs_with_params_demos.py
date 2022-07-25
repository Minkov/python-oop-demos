from decorators.measure_time import measure_time


@measure_time
def get_name():
    return 'Doncho Minkov'


@measure_time
def sum_two(x, y):
    return x + y


@measure_time
def sum_three(x, y, z):
    return x + y + z


@measure_time
def full_name(first_name, last_name):
    return first_name + ' ' + last_name


print(get_name())  # args=(), kwargs={}
print(sum_two(1, 2))
print(sum_three(1, 2, 3))  # args=(1, 2, 3), kwargs={}
print(sum_three(1, 2, z=3))  # args=(1, 2),  kwargs={'z':3}
print(full_name('Doncho', 'Minkov'))
