# Generated by Django 4.1.4 on 2022-12-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_book_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Картинка книги'),
        ),
    ]
