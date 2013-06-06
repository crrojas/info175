#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

#http://pastie.org/7984116

def connect():
    con = sqlite3.connect('movies.db')
    con.row_factory = sqlite3.Row
    return con


def get_countries():
    con = connect()
    c = con.cursor()
    query = """SELECT id_country, name FROM countries"""
    result = c.execute(query)
    countries = result.fetchall()
    con.close()
    return countries


def get_movies():
    con = connect()
    c = con.cursor()
    query = """SELECT a.id_movie, a.title, a.year_of_release, a.director, b.name as 'country'
            FROM movies a, countries b WHERE a.fk_id_country = b.id_country"""
    result = c.execute(query)
    movies = result.fetchall()
    con.close()
    return movies

def get_movies_by_country(id_country):
    con = connect()
    c = con.cursor()
    query = """SELECT a.id_movie, a.title, a.year_of_release, a.director, b.name as 'country'
            FROM movies a, countries b WHERE a.fk_id_country = b.id_country
            AND a.fk_id_country = ?"""
    result = c.execute(query, [id_country])
    movies = result.fetchall()
    con.close()
    return movies

def search_movies(word):
    con = connect()
    c = con.cursor()
    query = """SELECT a.id_movie, a.title, a.year_of_release, a.director, b.name as 'country'
            FROM movies a, countries b WHERE a.fk_id_country = b.id_country
            AND (a.title LIKE '%'||?||'%' OR a.director LIKE '%'||?||'%' OR b.name LIKE '%'||?||'%' )"""

    result = c.execute(query, [word, word, word])
    movies = result.fetchall()
    con.close()
    return movies