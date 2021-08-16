from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# Create your views here.

def create_table(request):
    try:
        conn = psycopg2.connect('dbname=djangotraining user=djangouser password=secret')
        cur = conn.cursor()
        cur.execute("CREATE TABLE ex00_movies ( \
            title varchar(64) NOT NULL UNIQUE, \
            episode_nb int PRIMARY KEY, \
            opening_crawl text NULL, \
            director varchar(32) NOT NULL, \
            producer varchar(128) NOT NULL, \
            release_date date NOT NULL);")
        conn.commit()
        cur.close()
        conn.close()
    except Exception as err:
        return(HttpResponse(err))
    return (HttpResponse("OK"))
