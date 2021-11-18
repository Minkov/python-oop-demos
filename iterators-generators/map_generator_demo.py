ll = [1, 2, 3]


def increment(x):
    print(f'Old value: {x}')
    return x + 1


print(map(increment, ll))

for x in map(increment, ll):
    print(x)

iter = map(increment, ll)
