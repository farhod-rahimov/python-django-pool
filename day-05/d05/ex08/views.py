from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

from django.contrib.staticfiles import finders

# Create your views here.

def create_table(request):
    try:
        conn = psycopg2.connect('dbname=djangotraining user=djangouser password=secret')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE  ex08_planets  (\
            id SERIAL PRIMARY KEY, \
            name varchar(64) NOT NULL UNIQUE, \
            climate varchar, \
            diameter int4, \
            orbital_period int4, \
            population int8, \
            rotation_period int4, \
            surface_water real, \
            terrain varchar(128));")

        cursor.execute("CREATE TABLE ex08_people (\
            id SERIAL PRIMARY KEY, \
            name varchar(64) NOT NULL UNIQUE, \
            birth_year varchar(32), \
            gender varchar(32), \
            eye_color varchar(32), \
            hair_color varchar(32), \
            height int4, \
            mass real, \
            homeworld varchar(64), \
            FOREIGN KEY (homeworld) REFERENCES ex08_planets (name));")
        
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as err:
        return(HttpResponse(err))

    return (HttpResponse("OK"))

def populate(request):
    return_msg = ""
    try:
        conn = psycopg2.connect('dbname=djangotraining user=djangouser password=secret')
        cursor = conn.cursor()
        with open(str(finders.find('ex08/people.csv')), 'r') as f:
        
        data = list("")
        i = 0
        for a in f:
            if a == '\n':
                i+
            data[i] += a

            cursor.copy_from(f, 'ex08_people', sep=' ')
            return_msg += "OK" + "<br>"
    except Exception as err:
        return_msg += str(err) + "<br>"

    conn.commit()
    cursor.close()
    conn.close()
    return HttpResponse(return_msg)

def display(request):
    try:
        conn = psycopg2.connect('dbname=djangotraining user=djangouser password=secret')
        cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        cursor.execute("select * from ex06_movies")
        data = cursor.fetchall()
    except Exception as err:
        return HttpResponse("No data available")

    cursor.close()
    conn.close()
    return render(request, 'ex06/display_movies.html', {'data': data})
