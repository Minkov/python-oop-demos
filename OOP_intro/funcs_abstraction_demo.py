def get_name(number):
    if number == 1:
        return 'One'
    elif number == 2:
        return 'Two'
    else:
        return number


# enables extensibility
def print_list(ll):
    for x in ll:
        if x is None:
            continue
        print(get_name(x))


ll1 = [1, 2, 3, 4, 5, 6]
print('Printing fist list')
print_list(ll1)
# print(ll1)

ll2 = [6, 5, 4, 3, None, 2, 1, None]
print('Printing second list')
print_list(ll2)
# print(ll2)
