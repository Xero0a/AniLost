# Generated by Django 4.1.6 on 2023-03-23 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Аниме')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='img/', verbose_name='Картинка')),
                ('jumbotron', models.ImageField(upload_to='img/', verbose_name='Главная картинка')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_genre', models.CharField(max_length=120, verbose_name='Жанр')),
            ],
        ),
        migrations.CreateModel(
            name='AnimeGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='anime', to='main.anime')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='genre', to='main.genre')),
            ],
        ),
        migrations.AddField(
            model_name='anime',
            name='genre',
            field=models.ManyToManyField(through='main.AnimeGenre', to='main.genre'),
        ),
    ]
