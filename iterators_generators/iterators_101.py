'''
`__iter__()` - internal dunder method in class
`iter()` - external from the class function, that calls `__iter__``
'''
ll = [1, 2, 3, 4, 5]

print(' --- With `for` loop ---')

for x in ll:
    print(x)

print(' --- Manual ---')
ll_iter = iter(ll)  # creates an iterator object for `ll`

print(ll_iter)
print(next(ll_iter))  # get `next` value
print(next(ll_iter))  # get `next` value
print(next(ll_iter))  # get `next` value
print(next(ll_iter))  # get `next` value

print(' --- With `while` loop')

ll_iter = iter(ll)
while True:
    try:
        print(next(ll_iter))
    except StopIteration:
        break
