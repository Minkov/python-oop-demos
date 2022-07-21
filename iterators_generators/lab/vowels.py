class vowels:
    vowel_chars = 'eyuioa'

    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):  # This work thanks to duck-typing
        return self

    def __next__(self):  # This work thanks to duck-typing
        while self.index < len(self.text):
            if self.text[self.index].lower() not in self.vowel_chars:
                self.index += 1
                continue

            value_to_return = self.text[self.index]
            self.index += 1
            return value_to_return

        raise StopIteration

    def iter_with_gen(self):
        return (x for x in self.text if x.lower() in self.vowel_chars)


my_string = vowels('Abcedifuty0o')
for char in my_string:  # This work thanks to duck-typing
    print(char)

for char in my_string.iter_with_gen():
    print(char)
