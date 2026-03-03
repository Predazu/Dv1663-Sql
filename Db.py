import mysql.connector




# startup config for accessing database
DB = mysql.connector.connect(
host ="",
user ="",
password ="",
database=""
)

DB_cursor = DB.cursor()



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
        
        if command_var == "exit"  == "Exit" == "9":
            exit = True
            print("Exiting...")
        if command_var == "1":
            multirelation_1()
            
        if command_var == "2":
            multirelation_2()
            
        if command_var == "3":
            grouping()
            
        if command_var == "4":
            join()
            
        if command_var == "5":
            function()
            
        if command_var == "6":
            trigger()
            
        if command_var == "7":
            procedure()
            
        if command_var == "8":
            aggregation()
            
        else:
            print("The number selected does not match any of the alternatives please try again.")
        


main()