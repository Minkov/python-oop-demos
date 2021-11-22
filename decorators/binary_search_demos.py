# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

def binary_search(values, target):
    def binary_search_internal(values, target, start, end):
        if start == end:
            return -1

        mid = (end + start) // 2
        if values[mid] == target:
            return mid
        elif values[mid] < target:
            return binary_search_internal(values, target, mid + 1, end)
        else:
            return binary_search_internal(values, target, start, mid)

    return binary_search_internal(values, target, 0, len(values))


print(binary_search([1, 2, 3, 4, 5, 6], 6))
print(binary_search([1, 2, 3, 4, 5, 6], 1))
print(binary_search([1, 2, 3, 4, 5, 6], 3))
print(binary_search([1, 2, 3, 4, 5, 6], 5))
print(binary_search([1, 2, 3, 4, 5, 6], 7))
