import json

def save_movies(movies):
    with open("movies.json", "w") as f:
        json.dump([movie.to_dict() for movie in movies], f, indent=4)

def load_movies():
    try:
        with open("movies.json", "r") as f:
            data = json.load(f)
            from movie import Movie
            return [Movie.from_dict(item) for item in data]
    except FileNotFoundError:
        return []