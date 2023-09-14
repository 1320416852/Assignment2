import sqlite3

# Read the file content into a list
with open('stephen_king_adaptations.txt', 'r') as file:
    stephen_king_adaptations_list = [line.strip().split(',') for line in file]

# Establish a connection with the database
conn = sqlite3.connect('stephen_king_adaptations.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table (
                    movieID TEXT,
                    movieName TEXT,
                    movieYear INTEGER,
                    imdbRating REAL
                )''')

# Insert data
cursor.executemany('INSERT INTO stephen_king_adaptations_table VALUES (?,?,?,?)', stephen_king_adaptations_list)

# Commit the changes
conn.commit()

# Search functionality
while True:
    print("Please select a movie search parameter:")
    print("1. Movie name")
    print("2. Movie year")
    print("3. Movie rating")
    print("4. STOP")

    option = input("Enter your choice: ")

    if option == '1':
        movie_name = input("Enter the movie name to search: ")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName=?", (movie_name,))
        result = cursor.fetchone()

        if result:
            print("Movie Name:", result[1])
            print("Movie Year:", result[2])
            print("IMDB Rating:", result[3])
        else:
            print("No such movie exists in our database.")

    elif option == '2':
        movie_year = input("Enter the movie year to search: ")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear=?", (movie_year,))
        results = cursor.fetchall()

        if results:
            for result in results:
                print("Movie Name:", result[1])
                print("Movie Year:", result[2])
                print("IMDB Rating:", result[3])
        else:
            print("No movies were found for that year in our database.")

    elif option == '3':
        rating = float(input("Enter the minimum movie rating to search: "))
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?", (rating,))
        results = cursor.fetchall()

        if results:
            for result in results:
                print("Movie Name:", result[1])
                print("Movie Year:", result[2])
                print("IMDB Rating:", result[3])
        else:
            print("No movies at or above that rating were found in the database.")

    elif option == '4':
        break

    print()

# Close the database connection
conn.close()
