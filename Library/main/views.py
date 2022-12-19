from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    books = Book.objects.all()
    render_books = []
    for book in books:
        about_book = {
            'title': book.title,
            'author': book.author,
            'img': request.build_absolute_uri(book.img.url),
            'active': book.in_library
        }
        render_books.append(about_book)
    return render(request, 'main/index.html', context={'books': render_books})
