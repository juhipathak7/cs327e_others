Query 1

SELECT * FROM genres
ORDER BY id_genres;

SELECT COUNT(*)
FROM movie_genres
WHERE id_genres=8 ;

Query 2

SELECT COUNT(*)
FROM movie_genres g
FULL OUTER JOIN movies m ON g.id_movies= m.id_movies
WHERE g.id_genres=8 AND m.year='2008';

Query 3

SELECT COUNT(*)
FROM actors a
JOIN casts c ON a.id_actors=c.id_actors
JOIN movies m ON c.id_movies=m.id_movies
WHERE a.gender= 'F' AND m.year= '2007';

Query 4

SELECT COUNT(*)			
FROM movies m
WHERE m.year= '2012' ;

Query 5

SELECT year, COUNT(*)
FROM movies
GROUP BY year
ORDER BY COUNT(*) DESC; 

Query 6

SELECT * FROM genres
ORDER BY id_genres;

SELECT COUNT(*)
FROM actors a
JOIN casts c ON a.id_actors=c.id_actors
JOIN movies m ON c.id_movies=m.id_movies
JOIN movie_genres g ON g.id_movies=m.id_movies
WHERE g.id_genres=23 and a.id_actors>0; 

Query 7

SELECT COUNT(*)
FROM actors WHERE first_name= 'Brad';

Query 8

SELECT COUNT(*), e.genres 
FROM movie_genres g
JOIN movies m ON g.id_movies= m.id_movies
JOIN genres e ON g.id_genres = e.id_genres
GROUP BY e.genres
ORDER BY COUNT(*) DESC;

Query 9

SELECT id_movies, COUNT(id_genres) FROM movie_genres
GROUP BY id_movies HAVING COUNT(movie_genres.id_genres)>8
ORDER BY COUNT(*) DESC;

Query 10

SELECT a.first_name, a.last_name, a.id_actors, COUNT(name) FROM aka_names k
JOIN actors a ON k.id_actors=a.id_actors
GROUP BY a.id_actors HAVING COUNT(k.name)>18
ORDER BY COUNT(*) DESC;
