import os

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    USER_EXISTS_ERROR_MESSAGE = 'User already exists!'
    USER_NOT_EXIST_ERROR_MESSAGE = 'This user does not exist!'
    MOVIE_UPLOADED_ERROR_MESSAGE = 'Movie already added to the collection!'

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []
        self.users_by_username = {}

    def register_user(self, username: str, age: int):
        """
        Creates an instance of the `User` class with the given username and age, and:
            - If the user (object) is not in the `users_collection` list, add him/her
                - return the message "{username} registered successfully."
            - If a user with the same username is already registered
                - raise an `Exception` with the message "User already exists!"
        """
        user = self.__get_user_by_username(username)

        if user:
            raise Exception(self.USER_EXISTS_ERROR_MESSAGE)

        user = User(username, age)
        self.users_collection.append(user)
        self.users_by_username[user.username] = user

        return f'{user.username} registered successfully.'

    def upload_movie(self, username: str, movie: Movie):
        """
        **Only the owner of the given movie can upload it.**
        The method adds the movie to the user's `movies_owned` list as well as the `movies_collection` list:
        - If the addition is successful, returns the message: "{username} successfully added {movie_title} movie."
        - If the user with the `username` provided is not registered in the app
            - Raise an `Exception` with the message: "This user does not exist!"
        - If the user exists, but he/she is not the owner of the given movie
            - Raise an `Exception` with the message: "{username_given} is not the owner of the movie {movie_title}!"
        - If the movie object is already uploaded
            - Raise an `Exception` with the message: "Movie already added to the collection!"
        """

        user = self.__get_user_by_username(username)

        self.__validate_user_exists(user)
        self.__validate_user_is_movie_owner(user, movie)
        self.__validate_movie_not_uploaded(movie)

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        """
        **Only the owner of the movie given can edit it. You will always be given usernames of registered users.**
        `kwargs` will be one or more key-value pairs:
            - The key will be a movie's attribute name ("title", "year", or "age_restriction")
            - The value will be the new value for that attribute
            - You will not receive anything different from the keys mentioned above

        The method edits the movie attributes with the given values and returns the message "{username} successfully edited {movie_title} movie."

        - If the movie is not uploaded
            - Raise an Exception with the message "The movie {movie_title} is not uploaded!"
        - If the user does not own that movie
            - raise an Exception with the message "{username given} is not the owner of the movie {movie_title}!"
        """

        user = self.__get_user_by_username(username)

        self.__validate_movie_uploaded(movie)
        self.__validate_user_is_movie_owner(user, movie)

        movie.title = kwargs.get('title', movie.title)
        movie.year = kwargs.get('year', movie.year)
        movie.age_restriction = kwargs.get('age_restriction', movie.age_restriction)
        # for key in ['title', 'year', 'age_restriction']:
        #     if key not in kwargs:
        #         continue
        #     setattr(movie, key, kwargs[key])

        # ^ Same as:
        # if 'age_restriction' in kwargs:
        #     movie.age_restriction = kwargs['age_restriction']
        # else:
        #     movie.age_restriction = movie.age_restriction

        return f'{user.username} successfully edited {movie.title} movie.'

    def delete_movie(self, username: str, movie: Movie):
        """
        **Only the owner of the movie given can delete it. You will always be given usernames of registered users.**

        Deletes the movie given in both `movies_collection` and user's `movies_owned` lists.
            - Return the message "{username} successfully deleted {movie_title} movie."

        - If the movie is not uploaded
            - Raise an Exception with the message "The movie {movie_title} is not uploaded!"
        - If the user does not own that movie
            - Raise Exception with the message "{username given} is not the owner of the movie {movie_title}!"
        """

        user = self.__get_user_by_username(username)

        self.__validate_movie_uploaded(movie)
        self.__validate_user_is_movie_owner(user, movie)

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f'{user.username} successfully deleted {movie.title} movie.'

    def like_movie(self, username: str, movie: Movie):
        """
            **Owners cannot like their own movies.**
            **You will always be given usernames of registered users and uploaded movies.**

        Increases the value of the movie attribute `likes` by 1 and adds the movie to the user's list movies_liked.
             - Return the message "{username} liked {movie_title} movie."

        - If the user is also the owner
            - Raise an Exception with the message "{username} is the owner of the movie {movie_title}!"
        - If the user already liked that movie
            - Raise an Exception with the message "{username} already liked the movie {movie_title}!"
        """

        user = self.__get_user_by_username(username)

        self.__validate_user_is_not_movie_owner(user, movie)
        self.__validate_user_not_liked_movie(user, movie)

        movie.likes += 1  # TODO: Extract method `movie.increase_likes()`
        user.movies_liked.append(movie)  # TODO: Extract method `user.like_movie(movie)

        return f'{user.username} liked {movie.title} movie.'

    def dislike_movie(self, username: str, movie: Movie):
        """
        **Only the user who has liked the movie can dislike it.**
        **You will always be given usernames of registered users and uploaded movies.**

        Decreases the value of the movie attribute likes by 1 and removes that movie from the user's movies_liked list
            - Return the message "{username} disliked {movie_title} movie."

        - If the user didn't like that movie in the first place
            - Raise an `Exception` with the message "{username} has not liked the movie {movie_title}!"
        """

        user = self.__get_user_by_username(username)

        self.__validate_user_liked_movie(user, movie)

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f'{user.username} disliked {movie.title} movie.'

    def display_movies(self):
        """
        Sorts all movies uploaded by the year in descending order, then by title
        - It should return the details() for each movie on separate lines in the format.
        - If there are no movies uploaded, it returns: "No movies found."
    """

        if not self.movies_collection:
            return 'No movies found.'

        sorted_movies = sorted(self.movies_collection, key=self.__movie_order_by)

        return os.linesep.join(m.details() for m in sorted_movies)

    def __str__(self):
        """
        Return a string on 2 lines for all users' usernames and movies titles in the following format:
            - "All users: {all users' usernames separated by a comma and a space ", "}"
                - If no users: "All users: No users."
            - "All movies: {all movies' titles separated by a comma and a space ", "}"
                - If no movies: "All movies: No movies."
        """
        users_string = 'No users.'
        movies_string = 'No movies.'

        if self.users_collection:
            users_string = ', '.join(u.username for u in self.users_collection)
        if self.movies_collection:
            movies_string = ', '.join(m.title for m in self.movies_collection)

        return f"""All users: {users_string}
All movies: {movies_string}"""

    def __get_user_by_username(self, username) -> User:
        # Complexity O(1), always
        return self.users_by_username.get(username, None)
        # Complexity O(n), n = len(users_collection)
        # user = [u for u in self.users_collection
        #         if u.username == username]
        #
        # return user[0]

    def __validate_user_exists(self, user):
        if user is None:
            raise Exception(self.USER_NOT_EXIST_ERROR_MESSAGE)

    def __validate_user_is_movie_owner(self, user, movie):
        if user != movie.owner:
            raise Exception(self.__build_not_movie_owner_error_message(user, movie))

    def __validate_user_is_not_movie_owner(self, user, movie):
        if user == movie.owner:
            raise Exception(self.__build_movie_owner_error_message(user, movie))

    def __is_movie_uploaded(self, movie):
        matching_movies = [m for m in self.movies_collection if m == movie]
        return len(matching_movies) > 0

    def __validate_movie_uploaded(self, movie):
        if not self.__is_movie_uploaded(movie):
            raise Exception(self.__build_movie_not_uploaded_error_message(movie))

    def __validate_movie_not_uploaded(self, movie):
        if self.__is_movie_uploaded(movie):
            raise Exception(self.MOVIE_UPLOADED_ERROR_MESSAGE)

    def __validate_user_liked_movie(self, user: User, movie: Movie):
        if movie not in user.movies_liked:
            raise Exception(self.__build_user_not_liked_movie(user, movie))

    def __validate_user_not_liked_movie(self, user: User, movie: Movie):
        if movie in user.movies_liked:
            raise Exception(self.__build_user_liked_movie(user, movie))

    @staticmethod
    def __build_not_movie_owner_error_message(user, movie):
        return f'{user.username} is not the owner of the movie {movie.title}!'

    @staticmethod
    def __build_movie_owner_error_message(user: User, movie: Movie):
        return f'{user.username} is the owner of the movie {movie.title}!'

    @staticmethod
    def __build_movie_not_uploaded_error_message(movie):
        return f'The movie {movie.title} is not uploaded!'

    @staticmethod
    def __build_user_liked_movie(user: User, movie: Movie):
        return f'{user.username} already liked the movie {movie.title}!'

    @staticmethod
    def __build_user_not_liked_movie(user: User, movie: Movie):
        return f'{user.username} has not liked the movie {movie.title}!'

    @staticmethod
    def __movie_order_by(movie: Movie):
        return -movie.year, movie.title
