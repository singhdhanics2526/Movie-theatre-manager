class Movie:
    def __init__(self, title, director, year, genre):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
    
    def to_dict(self):
        return {
            "title": self.title,
            "director": self.director,
            "year": self.year,
            "genre": self.genre
        }
    
    @staticmethod
    def from_dict(data):
        return Movie(data["title"], data["director"], data["year"], data["genre"])
    
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.director} - {self.genre}"