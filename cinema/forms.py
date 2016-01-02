from django import forms
from .models import Movie, MovieCrew, Artist

class MovieForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['title'].widget.attrs['disabled'] = True

    def clean_title(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.movie
        else:
            return self.cleaned_data['title']

    class Meta:
        model = Movie
        fields = '__all__'

class MovieCrewForm(forms.ModelForm):
    # movie = forms.TypedChoiceField(widget=forms.Select(attrs={'class': 'browser-default'}))
    class Meta:
        model = MovieCrew
        fields = '__all__'

class BaseMovieCrewFormSet(forms.formsets.BaseFormSet):
    def clean(self):
        if any(self.errors):
            return

        # movies = []
        # character_names = []
        # duplicates = False
        #
        # for form in self.forms:
        #     if form.cleaned_data:
        #         movie = form.cleaned_data['movie']
        #         character_name = form.cleaned_data['character_name']
        #         # Check that no two links have the same movie or character_name
        #         if movie and character_name:
        #             if movie in movies:
        #                 duplicates = True
        #             movies.append(movie)
        #
        #             if character_name in character_names:
        #                 duplicates = True
        #             character_names.append(character_name)
        #
        #         if duplicates:
        #             raise forms.ValidationError(
        #                 'Crew member must have unique movies and character_names.',
        #                 code='duplicate_links'
        #             )
        #
        #         # Check that all links have both an movie and character_name
        #         if character_name and not movie:
        #             raise forms.ValidationError(
        #                 'All crew members must have a movie.',
        #                 code='missing_movie'
        #             )
        #         elif movie and not character_name:
        #             raise forms.ValidationError(
        #                 'All links must have a character_name.',
        #                 code='missing_character_name'
        #                 )

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
