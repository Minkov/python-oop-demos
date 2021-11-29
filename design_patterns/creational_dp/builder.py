from creational_dp.house import House


class HousesBuilder:
    rooms_count = 0
    floors_count = 1
    has_garage = False
    has_electricity = False
    balconies_count = 0
    town = 'Unknown'
    has_pool = False

    def with_rooms_count(self, rooms_count):
        self.rooms_count = rooms_count
        return self

    def with_floors_count(self, floors_count):
        self.floors_count = floors_count
        return self

    def with_garage(self):
        self.has_garage = True
        return self

    def with_electricity(self):
        self.has_electricity = True
        return self

    def with_balconies_count(self, balconies_count):
        self.balconies_count = balconies_count
        return self

    def with_town(self, town):
        self.town = town
        return self

    def with_pool(self):
        self.has_pool = True
        return self

    def build(self):
        return House(self.floors_count,
                     self.has_garage,
                     self.has_electricity,
                     self.rooms_count,
                     self.balconies_count,
                     self.has_pool,
                     self.town
                     )


# Factory + Builder
class HousesFactory:
    def get_house_in_burgas(self, floors_count, rooms_count, balconies_count):
        builder = HousesBuilder()
        builder.with_town('Burgas')
        builder.with_floors_count(floors_count)
        builder.with_rooms_count(rooms_count)
        builder.with_balconies_count(balconies_count)
        return builder.build()

    def get_house_in_burgas_with_chaining(self, floors_count, rooms_count, balconies_count):
        return HousesBuilder() \
            .with_town('Burgas') \
            .with_floors_count(floors_count) \
            .with_rooms_count(rooms_count) \
            .with_balconies_count(balconies_count) \
            .build()


builder = HousesBuilder()
builder.with_town('Sofia')
builder.with_floors_count(3)
builder.with_electricity()

house = builder.build()
print(house)

# Factories are abstractions over constructors(__init__)
# Builders are abstractions over factories
