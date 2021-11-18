def for_loop_recursion(iterable):
    def for_loop_internal(iterable_iter):
        try:
            print(next(iterable_iter))
            for_loop_internal(iterable_iter)
        except StopIteration:
            return

    return for_loop_internal(iter(iterable))


def for_loop(iterable):
    ii = iter(iterable)
    while True:
        try:
            print(next(ii))
        except StopIteration:
            break


# for_loop([1, 2, 3, 4, 7])
# for_loop({1, 2, 3, 4, 7})
# for_loop('Doncho')

ll = 'Doncho'

iter1 = iter(ll)
iter2 = iter(ll)

print(f'Iter 1: {next(iter1)}')
print(f'Iter 1: {next(iter1)}')
print(f'Iter 1: {next(iter1)}')

print(f'Iter 2: {next(iter2)}')

print(f'Iter 1: {next(iter1)}')

print(f'Iter 2: {next(iter2)}')

# for_loop_recursion(ll)
# ll_iter = iter(ll)
# ll_iter = ll.__iter__()
# print(ll_iter)
#
# print(next(ll_iter))
# print(next(ll_iter))
# print(next(ll_iter))
# print(next(ll_iter))
# print(next(ll_iter))
# print(next(ll_iter))
#
# print(ll)
