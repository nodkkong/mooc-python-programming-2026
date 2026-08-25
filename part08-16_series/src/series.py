# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        genres_string = ", ".join(genres)
        self.genres_string = genres_string
        self.ratings = 0
        self.counts = 0

    def rate(self, rating: int):
        self.ratings += rating
        self.counts += 1


    def __str__(self):
        if self.counts == 0:
            ratings_str = "no ratings"
        else:
            ratings_str = f"{self.counts} ratings, average {self.ratings / self.counts:.1f} points"
        return f"{self.title} ({self.seasons} seasons)\ngenres: {self.genres_string}\n{ratings_str}"

def minimum_grade(rating: float, series_list: list):
    result = []
    for series in series_list:
        if series.counts > 0 and series.ratings / series.counts >= rating:
            result.append(series)
    return result

def includes_genre(genre: str, series_list: list):
    result = []
    for series in series_list:
        if genre in series.genres:
            result.append(series)
    return result


