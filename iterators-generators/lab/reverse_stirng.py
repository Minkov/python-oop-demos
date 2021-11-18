# Wrong, not lazy
def reverse_text_wrong(text):
    for c in text[::-1]:
        yield c


def reverse_text_wrong2(text):
    return reversed(text)


def reverse_text(text):
    # correct
    # return (text[i] for i in range(len(text) - 1, -1, -1))

    # correct, but better
    index = -1
    while abs(index) < len(text) + 1:
        yield text[index]
        index -= 1


for char in reverse_text("step"):
    print(char, end='')
