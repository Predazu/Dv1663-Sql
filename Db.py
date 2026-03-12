import mysql.connector
import csv




# startup config for accessing database
DB = mysql.connector.connect(
host ="localhost",
user ="root",
password ="1234",
database="Final_project"
)

DB_cursor = DB.cursor()



def Csv_porter(): # imports data from the Datafolder into the database tables

    with open("data/Cinemas.csv", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                DB_cursor.execute("Insert Ignore Into Cinemas (cinema_id, name, location ) Values (%s, %s, %s)", row)
    DB.commit()

    with open("data/DirectorData.csv", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                DB_cursor.execute("Insert Ignore Into Director (director_id, name, country_of_origin, date_of_birth ) Values (%s, %s, %s, %s)", row)
    DB.commit()

    with open("data/Movies.csv", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                DB_cursor.execute("Insert Ignore Into Movies (movie_id, title, movie_genre, release_date, director_id ) Values (%s, %s, %s, %s, %s)", row)
    DB.commit()

    with open("data/MovieWatchers.csv", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                DB_cursor.execute("Insert Ignore Into MovieWatcher (watcher_id, username, favorite_genre, favorite_movie, favorite_director ) Values (%s, %s, %s, %s, %s)", row)
    DB.commit()

    with open("data/Reviews.csv", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                DB_cursor.execute("Insert Ignore Into Review (review_id, movie_id, watcher_id, user_score ) Values (%s, %s, %s, %s)", row)
    DB.commit()

    with open("data/ShowList.csv", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                DB_cursor.execute("Insert Ignore Into Shows (cinema_id, movie_id, show_date, show_time, screen ) Values (%s, %s, %s, %s, %s)", row)
    DB.commit()


def join(): #Lists how many Movies of each genre directors have made.

    DB_cursor.execute("""SELECT d.name AS Director,
                       m.movie_genre AS Genre,
                       COUNT(m.movie_genre) AS Amount FROM Director d
                       JOIN Movies m ON m.director_id = d.director_id
                       GROUP BY d.name, m.movie_genre 
                       ORDER BY d.name DESC;""")
    result = DB_cursor.fetchall()
    for i in result:
        print(i)
    return


def function(): # Gives the age of a director when they released the specified movie

    movie_key = input("""
You have selected Age of director!
which movie would you like to lookup?
the movies to lookup have the following id's:
                        
1)  Inception
2)  Interstellar
3)  Oppenheimer
4)  Parasite
5)  Gladiator
6)  Joker
""")
    

    #DB_cursor.execute(f"""Select how_old({movie_key})""")

    #DB_cursor.fetchone()


# problem currently där den visar alla filmer
    DB_cursor.execute(f"""SELECT m.title AS Movie, d.name AS Director, how_old(m.movie_id) AS Age 
    FROM Movies m 
    JOIN Director d ON m.director_id = d.director_id;
    WHERE m.movie_id = {movie_key}""")
    
    result = DB_cursor.fetchall()

    for i in result:
        print(i)
    return


def procedure(): # Show desired users favourite movies, genres
    print("""which user would you like to know more about?
User id, Username""")

    DB_cursor.execute("select watcher_id, username from Moviewatcher ")
    Users = DB_cursor.fetchall()
    for i in Users:
        print(i)

    DB_cursor.nextset() 
    user_id = input("please enter user id: ")
    DB_cursor.callproc("Get_user_favorites",(user_id,))
    for result in DB_cursor.stored_results():

        
        """ this gives a deprecation warning on first run however it works"""



        for i in result.fetchall():
            print(i)
    print("username, Favorite movie, Favorite director, Favorite genre")
    return


def Movie_Showings(): # Movie showings
    print("""
You have selected Movie showings!
Which movie would you like to know about?
Movie id, Title
""")
    DB_cursor.execute("select movie_id, title from Movies ")
    Movies = DB_cursor.fetchall()
    for i in Movies:
        print(i)
    
    Movie_id = input("please enter movie id: ")

    
    DB_cursor.execute("""Select m.title As Movie, s.screen As Screen, DATE_FORMAT(s.show_date, '%Y-%m-%d'),
                        DATE_FORMAT(s.show_time, '%H:%i'), c.name As Cinema,
                        c.location As location From Movies m
                        Join Shows s On m.movie_id = s.movie_id 
                        Join Cinemas c On s.cinema_id = c.cinema_id 
                        Where m.movie_id = """ + Movie_id)
    result = DB_cursor.fetchall()
    print("Title,Screen,Date,Time,Cinema,Location")
    for i in result:
        print(i)

    return 


def reviews(): # shows reviews for a desired movie
    movie_key = input(""" 
You have selected Movie reviews!
Which movie would you like to look up?
The available movies to lookup have the following id's:
                      
1)  Inception
2)  Interstellar
3)  Oppenheimer
4)  Parasite
5)  Gladiator
6)  Joker
""")
    DB_cursor.execute(f"""SELECT m.title AS Movie,
                       r.user_score AS Review,
                       mw.username AS Reviewer FROM Review r JOIN Movies m ON r.movie_id = m.movie_id
                       JOIN MovieWatcher mw ON r.watcher_id = mw.watcher_id WHERE m.movie_id = {movie_key};""")
    result = DB_cursor.fetchall()
    for i in result:
        print(i)

    return 


def main():

    Csv_porter()
    exit = False

    while exit == False:
        command_var=input(""" 
                          
                        Please select a number related to an action.
                
1) List how many movies of each genre directors have made
2) Age of a director during specified movie's release
3) User favorites
4) Movie showings 
5) Movie Reviews 
6) Exit
: """)

        if command_var == "6":
            exit = True
            print("Exiting...")
            
        elif command_var == "1":
            join()
            
        elif command_var == "2":
            function()

        elif command_var == "3":
            procedure()
            
        elif command_var == "4":
            Movie_Showings()
        
        elif command_var == "5":
            reviews()
            
        else:
            print("your choice was: "+ command_var)
            print("The number selected does not match any of the alternatives please try again.")
        


main()