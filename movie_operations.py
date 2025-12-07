import json
from movie import Movie
from movie_data import save_movies

def add_movie(movies):
    title = input("Enter movie title: ")
    director = input("Enter director: ")
    year = input("Enter year: ")
    genre = input("Enter genre: ")
    
    movie = Movie(title, director, year, genre)
    movies.append(movie)
    save_movies(movies)
    print("Movie added successfully!")

def view_movies(movies):
    if not movies:
        print("No movies in collection.")
        return
    
    print("\n--- Movie Collection ---")
    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie}")

def search_movie(movies):
    search_term = input("Enter movie title to search: ").lower()
    found = False
    
    for movie in movies:
        if search_term in movie.title.lower():
            print(f"Found: {movie}")
            found = True
    
    if not found:
        print("Movie not found.")

def delete_movie(movies):
    """Delete a movie from the collection"""
    if not movies:
        print("No movies in collection to delete.")
        return
    
    # Show all movies with numbers
    view_movies(movies)
    
    try:
        movie_num = int(input("\nEnter the movie number to delete: "))
        if 1 <= movie_num <= len(movies):
            deleted_movie = movies.pop(movie_num - 1)
            save_movies(movies)
            print(f"Deleted movie: {deleted_movie}")
        else:
            print("Invalid movie number. Please try again.")
    except ValueError:
        print("Please enter a valid number.")