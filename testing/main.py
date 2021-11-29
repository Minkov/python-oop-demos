def add(x, y):
    return x + y


def test_add__when_1_and_2__expect_3():
    # arrange
    expected = 3

    # act
    actual = add(1, 2)

    # assert
    if actual == expected:
        print('Ok')
    else:
        print('Wrong')


def test_add__when_2_and_1__expect_3():
    expected = 3
    actual = add(2, 1)
    if actual == expected:
        print('Ok')
    else:
        print('Wrong')


def test_add__when_5_and_minus5__expect_0():
    expected = 0
    actual = add(5, -5)
    if actual == expected:
        print('Ok')
    else:
        print('Wrong')


def test_add__when_None_and_2__expect_exception():
    expected = 0
    actual = add(None, 2)
    if actual == expected:
        print('Ok')
    else:
        print('Wrong')


# test_add__when_None_and_2__expect_exception()
# test_add__when_1_and_2__expect_3()
# test_add__when_2_and_1__expect_3()
# test_add__when_5_and_minus5__expect_0()
# 1, 2 => 3
# 2, 1 => 3
# 5, -5 => 0
# 0, 0 => 0
# None, None => Exception
# '1', 2 => Exception
