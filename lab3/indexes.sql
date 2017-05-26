
--Query 1

CREATE INDEX moviegenres_idgenres_idx ON movie_genres(id_genres);    

--Query 2

CREATE INDEX moviegenres_idmovies_idx ON movie_genres(id_movies); 
CREATE INDEX movies_idmovies_idx ON movies(id_movies);          
CREATE INDEX movies_year_idx ON movies(year);                     
--CREATE INDEX moviegenres_idgenres_idx ON movie_genres(id_genres);    Any code that has been commented out is indexes that are duplicates

--Query 3

CREATE INDEX actors_idactors_idx ON actors(id_actors);
CREATE INDEX cast_idactors_idx ON casts(id_actors);
CREATE INDEX cast_idmovies_idx ON casts(id_movies);
--CREATE INDEX movies_idmovies_idx ON movies(id_movies);    
CREATE INDEX actors_gender_idx ON actors(gender);
--CREATE INDEX movies_year_idx ON movies(year);        


--Query 4

--CREATE INDEX movies_year_idx ON movies(year);

--Query 5

--No query needed

--Query 6
--CREATE INDEX actors_idactors_idx ON actors(id_actors);
--CREATE INDEX cast_idactors_idx ON casts(id_actors);
--CREATE INDEX cast_idmovies_idx ON casts(id_movies);
--CREATE INDEX movies_idmovies_idx ON movies(id_movies);  
--CREATE INDEX moviegenres_idmovies_idx ON movie_genres(id_movies); 
--CREATE INDEX moviegenres_idgenres_idx ON movie_genres(id_genres);  
CREATE INDEX actors_idmovies_idx ON actors(id_actors);


--Query 7

CREATE INDEX actors_name_idx ON actors(first_name);

--Query 8

--CREATE INDEX moviegenres_idmovies_idx ON movie_genres(id_movies);
--CREATE INDEX movies_idmovies_idx ON movies(id_movies); 
<<<<<<< HEAD
CREATE INDEX movies_idgenres_idx ON movie_genres(id_genres);
=======
--CREATE INDEX movies_idgenres_idx ON movie_genres(id_genres);
>>>>>>> origin/master
CREATE INDEX genres_idgenres_idx ON genres(id_genres);

--Query 9

--No index needed

--Query 10

CREATE INDEX akanames_idactors ON aka_names(id_actors);
--CREATE INDEX actors_idactors_idx ON actors(id_actors);
