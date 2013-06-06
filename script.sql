http://codepad.org/Zsxspow8



CREATE TABLE countries (
id_country integer PRIMARY KEY AUTOINCREMENT,
name text NOT NULL)

INSERT INTO countries (name) VALUES ("USA");
INSERT INTO countries (name) VALUES ("ITALY");
INSERT INTO countries (name) VALUES ("CHILE");

CREATE TABLE movies (
id_movie integer PRIMARY KEY AUTOINCREMENT,
title text,
year_of_release integer,
director text,
fk_id_country integer,
FOREIGN KEY (fk_id_country) REFERENCES countries(id_country)
)

INSERT INTO movies (title, year_of_release, director, fk_id_country) 
VALUES ("The Shawshank Redemption", 1994, "Frank Darabont", 1);
INSERT INTO movies (title, year_of_release, director, fk_id_country) 
VALUES ("The Godfather", 1972, "Francis Ford Coppola", 1);
INSERT INTO movies (title, year_of_release, director, fk_id_country) 
VALUES ("Pulp Fiction", 1992, "Quentin Tarantino", 1);
INSERT INTO movies (title, year_of_release, director, fk_id_country) 
VALUES ("C'era una volta il West", 1968, "Sergio Leone", 2);
INSERT INTO movies (title, year_of_release, director, fk_id_country) 
VALUES ("La vita e bella", 1997, "Roberto Benigni", 2);
INSERT INTO movies (title, year_of_release, director, fk_id_country) 
VALUES ("Taxi para tres", 2001, "Orlando Lubbert", 3);