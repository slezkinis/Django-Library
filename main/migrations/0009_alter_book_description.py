# Generated by Django 4.1.4 on 2022-12-28 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание книги'),
        ),
    ]
