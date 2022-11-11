from django.urls import path

from .views import (
    BookCreateView,
    HomeView,
    BookListView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView,
    AuthorListView,
    AuthorCreateView,
    AuthorUpdateView,
    AuthorBooksListView,
    AuthorDeleteView,
    PublisherListView,
    PublisherCreateView,
    PublisherUpdateView,
    PublisherBooksListView,
    PublisherDeleteView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('books', BookListView.as_view(), name='book_list'),
    path('book/create', BookCreateView.as_view(), name='book_create'),
    path('book/<pk>', BookDetailView.as_view(), name='book_detail'),
    path('book/<pk>/update', BookUpdateView.as_view(), name='book_update'),
    path('book/<pk>/delete', BookDeleteView.as_view(), name='book_delete'),

    path('authors', AuthorListView.as_view(), name='author_list'),
    path('author/create', AuthorCreateView.as_view(), name='author_create'),
    path('author/<pk>/update', AuthorUpdateView.as_view(), name='author_update'),
    path('author/<pk>/books', AuthorBooksListView.as_view(), name='author_books'),
    path('author/<pk>/delete', AuthorDeleteView.as_view(), name='author_delete'),

    path('publishers', PublisherListView.as_view(), name="publisher_list"),
    path('publisher/create', PublisherCreateView.as_view(), name="publisher_create"),
    path('publisher/<pk>/update', PublisherUpdateView.as_view(), name="publisher_update"),
    path('publisher/<pk>/books', PublisherBooksListView.as_view(), name="publisher_books"),
    path('publisher/<pk>/delete', PublisherDeleteView.as_view(), name="publisher_delete"),
]
