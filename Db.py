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
                DB_cursor.execute("Insert Into Cinemas (cinema_id, name, location ) Values (%s, %s, %s)", row)
    DB.commit()

    with open("data/DirectorData.csv", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                DB_cursor.execute("Insert Into Director (director_id, name, country_of_origin, date_of_birth ) Values (%s, %s, %s, %s)", row)
    DB.commit()

    with open("data/Movies.csv", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                DB_cursor.execute("Insert Into Movies (movie_id, title, movie_genre, release_date, director_id ) Values (%s, %s, %s, %s, %s)", row)
    DB.commit()

    with open("data/MovieWatchers.csv", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                DB_cursor.execute("Insert Into MovieWatcher (watcher_id, username, favorite_genre, favorite_movie, favorite_director ) Values (%s, %s, %s, %s, %s)", row)
    DB.commit()

    with open("data/Reviews.csv", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                DB_cursor.execute("Insert Into Review (review_id, movie_id, watcher_id, user_score ) Values (%s, %s, %s, %s)", row)
    DB.commit()

    with open("data/ShowList.csv", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                DB_cursor.execute("Insert Into Shows (cinema_id, movie_id, show_date, show_time, screen ) Values (%s, %s, %s, %s, %s)", row)
    DB.commit()








def multirelation_1(): # skriv funktionallityeten här och bättre namn


    DB_cursor.execute("")
    result = DB_cursor.fetchall()
    for i in result:
        print(i)
    return

def multirelation_2(): # skriv funktionallityeten här och bättre namn


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

    DB_cursor.execute("SELECT d.name AS Director, m.movie_genre AS Genre, " \
    "COUNT(m.movie_genre) AS Amount " \
    "FROM Director d " \
    "JOIN Movies m ON m.director = d.director_id " \
    "GROUP BY d.name, m.movie_genre " \
    "ORDER BY d.name DESC")
    result = DB_cursor.fetchall()
    for i in result:
        print(i)
    return

def function(): # skriv funktionallityeten här och bättre namn


    DB_cursor.execute("")
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








def main():

    Csv_porter()
    exit = False

    while exit == False:
        command_var=input(""" 
                          
                        Please select a number related to an action.
                
1) Query 1
2) Query 2
3) Query 3
4) List how many movies of each genre directors have made
5) Query 5
6) Query 6
7) Query 7
8) Avg moviescore for a specific director. 
9) Exit
: """)

        if command_var == "9":
            exit = True
            print("Exiting...")
            
            
        elif command_var == "1":
            multirelation_1()
            
        elif command_var == "2":
            multirelation_2()
            
        elif command_var == "3":
            grouping()
            
        elif command_var == "4":
            join()
            
        elif command_var == "5":
            function()
            
        elif command_var == "6":
            trigger()
            
        elif command_var == "7":
            procedure()
            
        elif command_var == "8":
            aggregation()
            
        else:
            print("your choice was: "+command_var)
            print("The number selected does not match any of the alternatives please try again.")
        


main()