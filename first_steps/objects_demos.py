print(isinstance(5, int))
print(isinstance(5.5, int))
print(isinstance(5, object))
print(isinstance(int, object))

print(isinstance([], object))

ll = [1, 2, 3]  # ll=list(1,2,3)
ll2 = []  # ll2=list()

print(ll)
ll.append(-4)
print(ll)
print(ll + [-6])
