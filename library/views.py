from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    ListView,
    DeleteView,
    TemplateView
)

from .models import (
    Book,
    Publisher,
    Author
)

from .forms import (
    BookForm,
    AuthorForm,
    PublisherForm
)


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_count = Book.objects.all().count()
        context['book_count'] = book_count
        author_count = Author.objects.all().count()
        context['author_count'] = author_count
        publisher_count = Publisher.objects.all().count()
        context['publisher_count'] = publisher_count
        return context


class BookListView(ListView):
    template_name = 'book_list.html'
    paginate_by = 10
    model = Book


class BookCreateView(CreateView):
    model = Book
    template_name = 'book_create.html'
    form_class = BookForm

    def get_success_url(self):
        next_page = self.request.GET.get('next', None)
        if next_page:
            return next_page
        return reverse('book_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Dodaj'
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_create.html'
    form_class = BookForm

    def get_success_url(self):
        next_page = self.request.GET.get('next', None)
        if next_page:
            return next_page
        return reverse('book_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Zaktualizuj'
        return context


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'

    def get_success_url(self):
        next_page = self.request.GET.get('next', None)
        if next_page:
            return next_page
        return reverse('book_list')


class AuthorListView(ListView):
    template_name = 'author_list.html'
    paginate_by = 10
    model = Author

    def get_queryset(self):
        return Author.objects.with_books()


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_create.html'
    form_class = AuthorForm

    def get_success_url(self):
        next_page = self.request.GET.get('next', None)
        if next_page:
            return next_page
        return reverse('author_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Dodaj'
        return context


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'author_create.html'
    form_class = AuthorForm

    def get_success_url(self):
        next_page = self.request.GET.get('next', None)
        if next_page:
            return next_page
        return reverse('author_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Zaktualizuj'
        return context


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_delete.html'

    def get_success_url(self):
        next_page = self.request.GET.get('next', None)
        if next_page:
            return next_page
        return reverse('author_list')


class AuthorBooksListView(ListView):
    template_name = 'author_book_list.html'
    paginate_by = 10

    def get_object(self):
        pk = self.kwargs.get('pk')
        author = get_object_or_404(Author.objects.with_books(), pk=pk)
        return author

    def get_queryset(self):
        return self.get_object().books.all()

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['object'] = self.get_object()
        return context


class PublisherListView(ListView):
    template_name = 'publisher_list.html'
    paginate_by = 10
    model = Publisher

    def get_queryset(self):
        return Publisher.objects.with_books()


class PublisherCreateView(CreateView):
    model = Publisher
    template_name = 'publisher_create.html'
    form_class = PublisherForm

    def get_success_url(self):
        next_page = self.request.GET.get('next', None)
        if next_page:
            return next_page
        return reverse('publisher_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Dodaj'
        return context


class PublisherUpdateView(UpdateView):
    model = Publisher
    template_name = 'publisher_create.html'
    form_class = PublisherForm

    def get_success_url(self):
        next_page = self.request.GET.get('next', None)
        if next_page:
            return next_page
        return reverse('publisher_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Zaktualizuj'
        return context


class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'publisher_delete.html'

    def get_success_url(self):
        next_page = self.request.GET.get('next', None)
        if next_page:
            return next_page
        return reverse('publisher_list')


class PublisherBooksListView(ListView):
    template_name = 'publisher_book_list.html'
    paginate_by = 10

    def get_object(self):
        pk = self.kwargs.get('pk')
        publisher = get_object_or_404(Publisher.objects.with_books(), pk=pk)
        return publisher

    def get_queryset(self):
        return self.get_object().book_set.all()

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['object'] = self.get_object()
        return context