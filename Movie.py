import csv

FILE = "movies.csv"

def load_data():
    movies = []
    try:
        with open(FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                movies.append(row)
    except:
        print("Error loading dataset!")
    return movies


def save_movie(title, genre, rating):
    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([title, genre, rating])
    print("Movie added successfully!")


def recommend_by_genre(movies):
    genre = input("Enter genre: ")
    results = [m for m in movies if genre.lower() in m['Genre'].lower()]
    
    if not results:
        print("No movies found!")
        return
    
    print("\n🎬 Recommended Movies:\n")
    for m in results:
        print(f"{m['Title']} (⭐ {m['Rating']})")


def top_movies(movies):
    sorted_movies = sorted(movies, key=lambda x: float(x['Rating']), reverse=True)
    
    print("\n🏆 Top Movies:\n")
    for m in sorted_movies[:5]:
        print(f"{m['Title']} (⭐ {m['Rating']})")


def filter_by_rating(movies):
    try:
        rating = float(input("Show movies above rating: "))
        results = [m for m in movies if float(m['Rating']) >= rating]
        
        print("\n⭐ Movies Found:\n")
        for m in results:
            print(f"{m['Title']} (⭐ {m['Rating']})")
    except:
        print("Invalid input!")


def add_movie():
    title = input("Enter movie title: ")
    genre = input("Enter genre: ")
    rating = input("Enter rating: ")
    save_movie(title, genre, rating)


def main():
    while True:
        movies = load_data()
        
        print("\n🍿 Movie Recommendation System")
        print("1. Recommend by Genre")
        print("2. Top Movies")
        print("3. Filter by Rating")
        print("4. Add New Movie")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            recommend_by_genre(movies)
        elif choice == '2':
            top_movies(movies)
        elif choice == '3':
            filter_by_rating(movies)
        elif choice == '4':
            add_movie()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
    