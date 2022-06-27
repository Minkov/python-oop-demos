# Global namespace - pi and sum1 (global for this module)
from math import pi


def f1():
    pi = 3.14
    print(pi)


def sum1(ll):
    # result and x - in local namespace (local for func body and class)
    result = 1
    for x in ll:
        result += x
    return result


# print and sum - built-in namespace
print(sum([1, 2, 3, 4]))
print(sum1([1, 2, 3, 4]))
print(pi)
f1()
print(pi)
