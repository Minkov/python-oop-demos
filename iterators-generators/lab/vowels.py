class vowels:
    vowels = set('eyuioaEYUIOA')

    def __init__(self, text):
        self.text = text
        # Wrong
        self.vowels_in_text = [x for x in text if x in self.vowels]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # while self.index < len(self.text):
        #     if self.text[self.index] in self.vowels:
        #         value_to_return = self.text[self.index]
        #         self.index += 1
        #         return value_to_return
        #     self.index += 1

        while self.index < len(self.text) \
                and self.text[self.index] not in self.vowels:
            self.index += 1

        if self.index == len(self.text):
            raise StopIteration

        value_to_return = self.text[self.index]
        self.index += 1
        return value_to_return


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
