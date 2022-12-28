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
            'active': book.in_library,
            'id': book.id
        }
        render_books.append(about_book)
    return render(request, 'main/index.html', context={'books': render_books})


def show_book(request, book_id):
    book = Book.objects.get(id=book_id)
    about_book = {
        'title': book.title,
        'img': request.build_absolute_uri(book.img.url),
        'description': book.description,
        'author': book.author,
        'id': book_id
    }
    return render(request, 'main/book.html', context={'book': about_book})

