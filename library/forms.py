from django.forms import ModelForm

from .models import Book, Author, Publisher


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'page_count', 'publish_year']


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']
