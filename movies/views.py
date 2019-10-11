from django.shortcuts import render, redirect
from .models import movie

# Create your views here.
def index(request):
    movies = movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'index.html',context)

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        title_en = request.POST.get('title-en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open-date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch-grade')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster-url')
        description = request.POST.get('description')

        movie.objects.create(
            title = title,
            title_en = title_en,
            audience = audience,
            open_date = open_date,
            genre = genre,
            watch_grade = watch_grade,
            score = score,
            poster_url = poster_url,
            description = description,
        )
        return redirect('movies:index')
    else:
        return render(request, 'form.html')

def detail(request, id):
    Movie=movie.objects.get(id=id)
    context = {
        'movies' : Movie,
    }
    return render(request,'detail.html',context)

def update(request, id):
    Movie=movie.objects.get(id=id)
    context = {
        'movies' : Movie,
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        title_en = request.POST.get('title-en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open-date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch-grade')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster-url')
        description = request.POST.get('description')

        Movie.title = title
        Movie.title_en = title_en
        Movie.audience = audience
        Movie.open_date = open_date
        Movie.genre = genre
        Movie.watch_grade = watch_grade
        Movie.score = score
        Movie.poster_url = poster_url
        Movie.description = description

        Movie.save()
        return redirect('movies:index')
    else:
        return render(request, 'edit.html', context)

    #  title = request.POST.get('title')
    #  title_en = request.POST.get('text_en')
    #  audience = request.POST.get('audience')
    #  open_date = request.POST.get('open_date')
    #  genre = request.POST.get('genre')
    #  watch_grade = request.POST.get('watch_grade')
    #  score = request.POST.get('score')
    #  poster_url = request.POST.get('poster_url')
    #  description = request.POST.get('description')
def delete(request, id):
    Movie=movie.objects.get(id=id)
    Movie.delete()

    return redirect('movies:index')