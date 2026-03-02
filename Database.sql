
CREATE DATABASE Final_project;
USE Final_project;
SET GLOBAL restrict_fk_on_non_standard_key = OFF;

DROP TABLE IF EXISTS Director;
CREATE TABLE Director (
	director_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country_of_origin VARCHAR(255),
    date_of_birth DATE
);



DROP TABLE IF EXISTS Movies;
CREATE TABLE Movies (
	movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    movie_genre VARCHAR(100),
    release_date DATE,
    director_id int,
    FOREIGN KEY (director_id) REFERENCES Director(director_id)
);

DROP TABLE IF EXISTS Cinemas;
CREATE TABLE Cinemas (
	cinema_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS MovieWatcher;
CREATE TABLE MovieWatcher (
	watcher_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    favorite_genre VARCHAR(100),
    favorite_movie INT,
    favorite_director INT,
    FOREIGN KEY (favorite_movie) REFERENCES Movies(movie_id)
		ON DELETE SET NULL
        ON UPDATE CASCADE,
	FOREIGN KEY	(favorite_director) REFERENCES Director(director_id)
		ON DELETE SET NULL
        ON UPDATE CASCADE
);



DROP TABLE IF EXISTS Review;
CREATE TABLE Review (
	review_id INT AUTO_INCREMENT PRIMARY KEY,
    user_score INT CHECK (user_score BETWEEN 1 AND 10),
    movie_id INT,
    watcher_id INT,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (watcher_id) REFERENCES MovieWatcher(watcher_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Shows;
CREATE TABLE Shows (
    cinema_id INT,
    movie_id INT,
    show_date DATE,
    show_time TIME,
    screen INT,
    PRIMARY KEY (cinema_id, movie_id, show_date, show_time),
    FOREIGN KEY (cinema_id) REFERENCES Cinemas(cinema_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

