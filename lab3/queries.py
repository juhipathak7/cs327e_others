# Feel free to define your own helper methods.
import psycopg2
from config import db

def connect():
    try:
        conn = psycopg2.connect(
            "dbname='" + db['DATABASE'] + "'" + 
            "user='" + db['USER'] + "'" + 
            "host='" + db['HOST'] + "'" + 
            "password='" + db['PASSWORD'] + "'"
            )
        cursor = conn.cursor()
        return cursor
    except:
        return None

def print_table(table):
    print("\n====RESULT TABLE====")

    cols = len(table[0])
    format_string = "%s " * cols
    for row in table:
        print (format_string % tuple(row))
    print("====================\n")

def run_query(query, cursor):
    cursor.execute(query)
    rows = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    rows.insert(0, colnames)
    return rows

def query_one(cursor):
    query= "SELECT * FROM genres ORDER BY id_genres;"
    result= run_query(query,cursor)
    print_table(result)
    enter= input('Select the id of the genre: ')
    query= "SELECT COUNT(*) FROM movie_genres WHERE id_genres = "+ str(enter)+ ";"
    result= run_query(query,cursor)
    print("The number of movies with the id genre " + str(enter)+ " is... ")
    print_table(result)

def query_two(cursor):
    query= "SELECT * FROM genres ORDER BY id_genres;"
    result=run_query(query,cursor)
    print_table(result)

    enter= input("Select the id of the genre: ")
    year= input("Select a year:")
    query="SELECT COUNT(*) FROM movie_genres g JOIN movies m ON g.id_movies= m.id_movies WHERE g.id_genres="+str(enter)+" AND m.year='"+ str(year) + "' ;" 
    result=run_query(query,cursor)
    print_table(result)

def query_three(cursor):
    year= input("Select a year: ")
    query= "SELECT COUNT(*) FROM actors a JOIN casts c ON a.id_actors=c.id_actors JOIN movies m ON c.id_movies=m.id_movies WHERE a.gender= 'F' AND m.year= '" + str(year)+ "';"
    result= run_query(query,cursor)
    print_table(result)

def query_four(cursor):
    year = input("Select a year: ")
    query = "SELECT COUNT(*) FROM movies m WHERE m.year= '"+ str(year) + "' ;"
    result= run_query(query,cursor)
    print_table(result)

def query_five(cursor):

    query = "SELECT year, COUNT(*) FROM movies GROUP BY year ORDER BY COUNT(*) DESC LIMIT 15; "
    result= run_query(query,cursor)
    print_table(result)

def query_six(cursor):

    query = "SELECT * FROM genres ORDER BY id_genres;"
    result= run_query(query,cursor)
    print_table(result)
    enter = input("Select the id of the genre:")
    query = "SELECT COUNT(*) FROM actors a JOIN casts c ON a.id_actors=c.id_actors JOIN movies m ON c.id_movies=m.id_movies JOIN movie_genres g ON g.id_movies=m.id_movies WHERE g.id_genres="+ str(enter) + " and a.id_actors>0; "
    result=run_query(query,cursor)
    print_table(result)  
 
def query_seven(cursor):
    name = input("Enter a name: ")
    query = "SELECT COUNT(*) FROM actors WHERE first_name= '"+ str(name) +"';"
    result= run_query(query,cursor)
    print_table(result)

def query_eight(cursor):

    query = "SELECT COUNT(*), e.genres FROM movie_genres g JOIN movies m ON g.id_movies= m.id_movies JOIN genres e ON g.id_genres = e.id_genres GROUP BY e.genres ORDER BY COUNT(*) DESC;"
    result= run_query(query,cursor)
    print_table(result)
    

def query_nine(cursor):
    genre_num = input("Enter number of genres: ")
    query = "SELECT id_movies, COUNT(id_genres) FROM movie_genres GROUP BY id_movies HAVING COUNT(movie_genres.id_genres)>" + genre_num +" ORDER BY COUNT(*) DESC;"
    result= run_query(query,cursor)
    print_table(result)

def query_ten(cursor):
    number= input("Enter a number of names: ")
    query = "SELECT a.first_name, a.last_name, a.id_actors, COUNT(name) FROM aka_names k JOIN actors a ON k.id_actors=a.id_actors GROUP BY a.id_actors HAVING COUNT(k.name)>"+number+" ORDER BY COUNT(*) DESC;"
    result= run_query(query,cursor)
    print_table(result)
