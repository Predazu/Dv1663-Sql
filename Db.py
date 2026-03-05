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








def multirelation_1(): # skriv funktionallityeten här och bättre namn


    DB_cursor.execute("")
    result = DB_cursor.fetchall()
    for i in result:
        print(i)
    return

def grouping(): # skriv funktionallityeten här och bättre namn


    DB_cursor.execute("")
    result = DB_cursor.fetchall()
    for i in result:
        print(i)
    return

def join(): #Lists how many Movies of each genre directors have made.

    DB_cursor.execute("SELECT d.name AS Director, m.movie_genre AS Genre, COUNT(m.movie_genre) AS Amount FROM Director d JOIN Movies m ON m.director = d.director_id GROUP BY d.name, m.movie_genre ORDER BY d.name DESC;")
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
2)	Interstellar
3)	Oppenheimer
4)	Parasite
5)  Gladiator
6)  Joker
""")
    DB_cursor.execute(f"""DROP FUNCTION IF EXISTS how_old; 
    DELIMITER $$ 
    CREATE FUNCTION how_old (movie_key INT) 
    RETURNS INT DETERMINISTIC 
    BEGIN 
    DECLARE age INT; 
    DECLARE rel_year INT; 
    DECLARE dir_yob INT; 
    SELECT YEAR(m.release_date), YEAR(d.date_of_birth) 
    INTO rel_year, dir_yob 
    FROM Movies m 
    JOIN Director d ON m.director = d.director_id AND m.movie_id = movie_key;
    SET age = rel_year - dir_yob;
    RETURN age;
    END; $$

    SELECT m.title AS Movie, d.name AS Director, how_old(m.movie_id) AS Age 
    FROM Movies m 
    JOIN Director d ON m.director = d.director_id;
    WHERE m.movie_id = {movie_key}""")
    result = DB_cursor.fetchall()
    for i in result:
        print(i)
    return

def trigger(): # skriv funktionallityeten här och bättre namn


    DB_cursor.execute("")
    result = DB_cursor.fetchall()
    for i in result:
        print(i)
    return

def procedure(): # skriv funktionallityeten här och bättre namn


    DB_cursor.execute("")
    result = DB_cursor.fetchall()
    for i in result:
        print(i)
    return


def aggregation(): # avg moviescore for director. 
    director_id = input("""
You have selected Avg moviescore for director!
which director would you like to lookup?
the available directors to lookup have the following id's:
                        
1)  Christopher Nolan	
2)	Bong Joon-ho	
3)	Ridley Scott	
4)	Todd Phillips
""")
    DB_cursor.execute("")
    result = DB_cursor.fetchall()
    for i in result:
        print(i)

    return 

def reviews():
    movie_key = input(""" 
You have selected Movie reviews!
Which movie would you like to look up?
The available movies to lookup have the following id's:
                      
1)  Inception
2)	Interstellar
3)	Oppenheimer
4)	Parasite
5)  Gladiator
6)  Joker
""")
    DB_cursor.execute(f"SELECT m.title AS Movie, r.user_score AS Review, mw.username AS Reviewer FROM Review r JOIN Movies m ON r.movie_id = m.movie_id JOIN MovieWatcher mw ON r.watcher_id = mw.watcher_id WHERE m.movie_id = {movie_key};")
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
                
1) Query 1
2) Query 2
3) List how many movies of each genre directors have made
4) Age of a director during specified movie's release
5) Query 5
6) Query 6
7) Avg moviescore for a specific director. 
8) Movie Reviews 
9) Exit
: """)

        if command_var == "9":
            exit = True
            print("Exiting...")
            
            
        elif command_var == "1":
            multirelation_1()
            
        elif command_var == "2":
            grouping()
            
        elif command_var == "3":
            join()
            
        elif command_var == "4":
            function()

        elif command_var == "5":
            trigger()

        elif command_var == "6":
            procedure()
            
        elif command_var == "7":
            aggregation()
        
        elif command_var == "8":
            reviews()
            
        else:
            print("your choice was: "+command_var)
            print("The number selected does not match any of the alternatives please try again.")
        


main()