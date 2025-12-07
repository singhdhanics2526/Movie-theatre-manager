from movie_data import load_movies
from movie_operations import add_movie, view_movies, search_movie, delete_movie

def main():
    movies = load_movies()
    
    while True:
        print("\n Movie Collection Manager")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Search Movie")
        print("4. Delete Movie")
        print("5. Exit")
        
        choice = input("Choose option (1-5): ")
        
        if choice == "1":
            add_movie(movies)
        elif choice == "2":
            view_movies(movies)
        elif choice == "3":
            search_movie(movies)
        elif choice == "4":
            delete_movie(movies)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()