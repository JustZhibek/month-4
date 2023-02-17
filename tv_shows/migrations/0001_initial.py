# Generated by Django 4.1.7 on 2023-02-16 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TVShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название фильма')),
                ('description', models.TextField(verbose_name='Описание фильма')),
                ('image', models.ImageField(upload_to='')),
                ('quantity', models.PositiveIntegerField(verbose_name='Колличество фильмов')),
                ('genre', models.CharField(choices=[('HORROR', 'HORROR'), ('COMEDY', 'COMEDY'), ('FANTASY', 'FANTASY'), ('THRILLER', 'THRILLER'), ('MELODRAMME', 'MELLODRAMME')], max_length=100)),
                ('video', models.URLField()),
                ('price', models.PositiveIntegerField(null=True, verbose_name='Цена билета')),
            ],
        ),
    ]
