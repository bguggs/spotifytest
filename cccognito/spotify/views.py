from django.shortcuts import render
from django.http import HttpResponse
import spotipy
import pprint
import sys

# Create your views here.
def spotify(request, query):
    sp = spotipy.Spotify()
    result = sp.search(query)
    pprint.pprint(result)
    return render(request, 'pages/home.html', {'results': result})



