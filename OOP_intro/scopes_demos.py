'''
scopes:
- Global scope (module)
- Function scope
- Class scope (from function scope)
'''


def print_greeting():
    text = 'Hello from func scope'
    print(text)


text = 'Hello from global'
text2 = 'Hello 2'


def f1():
    text = 'Hello from f1'

    def f1_inner():
        text = 'Hello from f1_inner'

        def f1_innermost():
            # text = 'Hello from f1_innermost'
            print(text)
            print(text2)

        print(text)
        f1_innermost()

    print(text)
    f1_inner()


def f1_rec():  # 1
    def f1_rec():  # 2
        def f1_rec():  # 3
            print('f1_rec 3')
            # f1_rec()

        print('f1_rec 2')
        f1_rec()  # checks local namespace, finds #3 and calls it

    print('f1_rec 1')
    f1_rec()  # checks local namespace, finds #2 and calls it


print_greeting()
print(text)
f1()
f1_rec()
