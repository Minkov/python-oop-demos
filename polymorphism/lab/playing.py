class Guitar:
    def play(self):
        return "Playing the guitar"


class Children:
    def play(self):
        return "Children are playing"

    def eat(self):
        return 'Children are eating'


def start_playing(i_can_play):
    return i_can_play.play()


children = Children()
guitar = Guitar()

print(start_playing(guitar))
print(start_playing(children))
