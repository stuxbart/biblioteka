from django.db import models
from django.db.models import Count


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField('Author', related_name='books')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True, blank=True)
    page_count = models.PositiveIntegerField(null=True, blank=True)
    publish_year = models.IntegerField(null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class PublisherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')

    def with_books(self):
        return self.get_queryset().annotate(book_count=Count('book'))


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = PublisherManager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class AuthorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('first_name', 'last_name')

    def with_books(self):
        return self.get_queryset().annotate(book_count=Count('books'))


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = AuthorManager()

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
