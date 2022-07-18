# Read numbers separated by a ' ', and print their sum
# Modification 1: print their sum divided by 2
# Modification 2: if the sum is even, print it divided by 2,
#       otherwise divided by 3
# Modification 3: return the result, don't print it

def sum2(numbers):
    the_sum = sum(numbers)
    if the_sum % 2 == 0:
        return the_sum / 2
    else:
        return the_sum / 3


numbers = [int(x) for x in input().split(' ')]

sum2(numbers)
