from urllib.parse import parse_qs
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Movie
from .forms import MovieForm
# Create your views here.

def movies(request):
    results = Movie.objects.all()
    context = {'movies': results}
    return render(request, 'movies_list.html', context)

def addMovie(request):
    form = MovieForm()

    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            messages.success(request, 'Movie was added successully!')
            return redirect('movies')

    context = {'form': form}
    return render(request, 'movie_form.html', context)
    

