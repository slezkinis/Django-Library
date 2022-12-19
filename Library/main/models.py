from django.db import models


class Book(models.Model):
    title = models.CharField('Название книги', max_length=150)
    author = models.CharField('Автор книги', max_length=150)
    img = models.ImageField(verbose_name='Картинка книги', upload_to='media')
    code = models.IntegerField('Персональный код книги')
    in_library = models.BooleanField('Наличие книги')

    def __str__(self) -> str:
        return self.title

