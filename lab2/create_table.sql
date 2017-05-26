\c postgres;
drop database if exists imdb;
create database imdb;
\c imdb;


create table Actors(
	id_actors int PRIMARY KEY NOT NULL UNIQUE,
	last_name varchar(1000),
	first_name varchar(1000),
	middle_name varchar(1000),
	gender int,
	number int);

create table Movies(
	id_movies int PRIMARY KEY NOT NULL UNIQUE,
	title varchar(1000),
	year int,
	number int,
	type int,
	location varchar(1000),
	language varchar(1000));

create table Keywords(
	id_keywords int PRIMARY KEY NOT NULL UNIQUE,
	keywords varchar(1000));

create table Series(
	id_series int PRIMARY KEY NOT NULL UNIQUE,
	id_movies int references Movies(id_movies),
	name varchar(1000),
	season int,
	number int);

create table Genres(
	id_genres int PRIMARY KEY NOT NULL UNIQUE,
	genres varchar(80) UNIQUE);

create table Casts(
	id_casts int PRIMARY KEY NOT NULL UNIQUE,
	id_movies int references Movies(id_movies),
	id_series int references Series(id_series),
	id_actors int references Actors(id_actors),
	character varchar(1500),
	billing_position int);

create table Movies_Keywords(
	id_movie_keyword int PRIMARY KEY NOT NULL UNIQUE,
	id_movies int references Movies(id_movies),
	id_keywords int references Keywords(id_keywords),
	id_series int references Series(id_series));

create table Aka_Names(
	id_aka_names int PRIMARY KEY NOT NULL UNIQUE,
	id_actors int references Actors(id_actors),
	name varchar(1000));

create table Aka_Titles(
	id_aka_titles int PRIMARY KEY NOT NULL UNIQUE,
	id_movies int references Movies(id_movies),
	title varchar(1000),
	location varchar(1000),
	year int);

create table Movie_Genres(
	id_movies_genres int PRIMARY KEY NOT NULL UNIQUE,
	id_movies int references Movies(id_movies),
	id_genres int references Genres(id_genres),
	id_series int references Series(id_series));

