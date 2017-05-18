from django import forms

from .models import books

class BookForm(forms.ModelForm):

    class Meta:
        model = books
        fields = ('title', 'year', 'rating',)

class SearchForm(forms.ModelForm):

    class Meta:
        model = books
        fields = ('title',)

class DeleteForm(forms.ModelForm):

    class Meta:
        model = books
        fields = ('title',)

class UpdateForm(forms.ModelForm):

    class Meta:
        model = books
        fields = ('title', 'year', 'rating',)