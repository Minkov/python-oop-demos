def f1():
    count = 0

    def f1_inner():
        def f1_innermost():
            nonlocal count  # get from parent scope
            count += 1

        f1_innermost()

    for _ in range(5):
        f1_inner()
        print(count)


def f1_2():
    count = [0]

    def f1_inner():
        def f1_innermost():
            count[0] += 1

        f1_innermost()

    for _ in range(5):
        f1_inner()
        print(count[0])


f1()
f1_2()
