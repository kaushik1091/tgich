from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import UpdateView
from django.forms import formset_factory
from django.db import IntegrityError, transaction
from django.contrib import messages
# from django.core.exceptions import ObjectDoesNotExist

from .models import Movie, MovieCrew, Artist
from .forms import MovieForm, MovieCrewForm, ArtistForm, BaseMovieCrewFormSet

def index(request):
    movies = Movie.objects.all()
    return render(request, "index.html", {'movies': movies})

def add_title(request):
    if request.method == "POST":
        movieForm = MovieForm(request.POST or None)
        if movieForm.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            movie_instance = movieForm.save(commit=False)
            movie_instance.save()
            return redirect('index')
    else:
        movieForm = MovieForm()

    return render(request, "add_title.html", {'movieForm': movieForm})

def del_title(request):
    try:
        if request.method == "GET":
            id = request.GET.get('id') or 0
            movie = Movie.objects.get(id=id)
            movie.delete()
        return redirect('index')
    except Movie.DoesNotExist:
        raise Http404("No movie matches the given id.")

# class UpdateMovie(UpdateView):
#     model = Movie
#     form_class = MovieForm
#     template_name = 'update_title.html'
#     success_url = '/'

def update_title(request, id):
    movie = get_object_or_404(Movie, id=id)
    movieForm = MovieForm(request.POST or None, instance=movie)
    MovieCrewFormSet = formset_factory(MovieCrewForm, formset=BaseMovieCrewFormSet, extra=10)

    movie_crew = MovieCrew.objects.filter(movie=movie)
    # crew_data = [{'artist':mc.artist, 'movie':movie, 'role':mc.role,
    #                 'character_name': mc.character_name} for mc in movie_crew]

    if request.method == 'POST':
        movieCrewFormSet = MovieCrewFormSet(request.POST)

        if movieForm.is_valid():
            movieForm.save()
            # return redirect('index')
        if movieCrewFormSet.is_valid():
            new_crew = []
            for movieCrewForm in movieCrewFormSet:
                # print(movieCrewForm.cleaned_data)
                artist = movieCrewForm.cleaned_data.get('artist')
                movie = movieCrewForm.cleaned_data.get('movie')
                role = movieCrewForm.cleaned_data.get('role')
                character_name = movieCrewForm.cleaned_data.get('character_name')

                if artist and movie and role and character_name:
                    new_crew.append(MovieCrew(artist=artist, movie=movie, role=role, character_name=character_name))

            try:
                with transaction.atomic():
                    MovieCrew.objects.filter(id=id).delete()
                    MovieCrew.objects.bulk_create(new_crew)

                    messages.success(request, 'You have updated the movie.')
            except IntegrityError: #If the transaction failed
                messages.error(request, 'There was an error saving the updated movie data.')
                return redirect(reverse('update_title'))
        else:
            print(movieCrewFormSet.errors)
    else:
        movieCrewFormSet = MovieCrewFormSet()
        # for form in movieCrewFormSet:
        #     form.fields['movie'].initial = movie

    return render(request, 'update_title.html', {'movie': movie, 'movieForm': movieForm,
                            'movieCrew':movie_crew, 'movieCrewFormSet': movieCrewFormSet})

def display_title(request):
    try:
        if request.method == "GET":
            # if request.method == "POST":

            id = request.GET.get('id') or 0
            movie = Movie.objects.get(id=id)
            return render(request, "title.html", {'movie': movie})
        else:
            return redirect('index')
    except Movie.DoesNotExist:
        raise Http404("No movie matches the given id.")

def add_artist(request):
    artists = Artist.objects.all()
    if request.method == "POST":
        artistForm = ArtistForm(request.POST or None)
        if artistForm.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            artist_instance = artistForm.save(commit=False)
            artist_instance.save()
    else:
        artistForm = ArtistForm()

    return render(request, "add_artist.html", {'artists': artists, 'artistForm': artistForm})
