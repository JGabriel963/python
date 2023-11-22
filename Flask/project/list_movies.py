import urllib.request
import json


def result_movies(type):
    if type == "Populares":
        url = "http://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=48e896d49084c8bfe5b85bc46870d1bc"
    elif type == "Animação":
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=48e896d49084c8bfe5b85bc46870d1bc"
    elif type == "2010":
        url = "http://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=48e896d49084c8bfe5b85bc46870d1bc"

    response = urllib.request.urlopen(url)

    data = response.read()

    data_json = json.loads(data)

    return data_json["results"]
