class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):
    def __init__(self):
        super().__init__()

    def add_movie(self, movie):
        self.movies.append(movie)
        return f"Комедии: {self.movies}"


class Drama(Movies):
    def __init__(self):
        super().__init__()

    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: {self.movies}"


c = Comedy()
d = Drama()

comedies = c.add_movie("Большой Куш")
print(comedies)

dramas = d.add_movie("Оружейный барон")
print(dramas)
