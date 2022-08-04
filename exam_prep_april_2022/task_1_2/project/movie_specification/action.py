from project.movie_specification.movie import Movie


class Action(Movie):
    MIN_AGE_RESTRICTION = 12

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = None):
        age_restriction = age_restriction if age_restriction else self.MIN_AGE_RESTRICTION
        super().__init__(title, year, owner, age_restriction)

    @property
    def type(self):
        return 'Action'
