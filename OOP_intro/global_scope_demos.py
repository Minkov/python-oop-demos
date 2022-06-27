prints_count = 0


def print_list(ll):
    # global makes `prints_count`
    # like an object of a reference type
    global prints_count

    prints_count += 1
    print(ll)


ll = list(range(5))

print(prints_count)
print_list(ll)
print(prints_count)
print_list(ll)
print(prints_count)
print_list(ll)
print(prints_count)
print_list(ll)
print(prints_count)
print_list(ll)
print(prints_count)
