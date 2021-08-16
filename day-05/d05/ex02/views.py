from django.db.models.base import Model
from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

from .models import Movies

# Create your views here.

def create_table(request):
    try:
        conn = psycopg2.connect('dbname=djangotraining user=djangouser password=secret')
        cur = conn.cursor()
        cur.execute("CREATE TABLE ex02_movies ( \
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

def populate(request):
    return_msg = ""
    data = [{'episode_nb' : 1, 'title' : 'The Phantom Menace',       'director' : 'George Lucas',    'producer' : 'Rick McCallum',                                       'release_date' : '1999-05-19'},
            {'episode_nb' : 2, 'title' : 'Attack of the Clones',     'director' : 'George Lucas',    'producer' : 'Rick McCallum',                                       'release_date' : '2002-05-16'},
            {'episode_nb' : 3, 'title' : 'Revenge of the Sith',      'director' : 'George Lucas',    'producer' : 'Rick McCallum',                                       'release_date' : '2005-05-19'},
            {'episode_nb' : 4, 'title' : 'A New Hope',               'director' : 'George Lucas',    'producer' : 'Gary Kurtz, Rick McCallum',                           'release_date' : '1977-05-25'},
            {'episode_nb' : 5, 'title' : 'The Empire Strikes Back',  'director' : 'Irvin Kershner',  'producer' : 'Gary Kurtz, Rick McCallum',                           'release_date' : '1980-05-17'},
            {'episode_nb' : 6, 'title' : 'Return of the Jedi',       'director' : 'Richard Marquand','producer' : 'Howard G. Kazanjian, George Lucas, Rick McCallum',    'release_date' : '1983-05-25'},
            {'episode_nb' : 7, 'title' : 'The Force Awakens',        'director' : 'J. J. Abrams',    'producer' : 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',          'release_date' : '2015-12-11'},
        ]

    for i in data:
        try:
            Movies.objects.create(episode_nb=i['episode_nb'], title=i['title'], director=i['director'],
                        producer=i['producer'], release_date=i['release_date'])
            return_msg += "OK" + "<br>"
        except Exception as err:
            return_msg += str(err) + "<br>"

    return HttpResponse(return_msg)

def display(request):
    data = Movies.objects.all()
    a = {'data': data}

    return render(request, 'ex02/display_movies.html', {'data': data})