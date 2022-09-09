from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Movie
from .forms import MovieForm
# Create your views here.

def movies(request):
    results = Movie.objects.all()
    context = {'movies': results}
    return render(request, 'movies_list.html', context)


@login_required(login_url='login')
@staff_member_required
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


@login_required(login_url='login')
@staff_member_required
def deleteMovie(request, pk):
    movie = Movie.objects.get(id=pk)
    if request.method == 'POST':
        movie.delete()
        messages.success(request, 'Movie deleted successfully!')
        return redirect('movies')
    context = {'object': movie}
    return render(request, 'delete_template.html', context)


@login_required(login_url='login')
@staff_member_required
def updateMovie(request, pk):
    movie = Movie.objects.get(id=pk)
    form = MovieForm(instance=movie)

    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie Updated!')
            return redirect('movies')

    context = {'form': form}
    return render(request, 'movie_form.html', context)
    

