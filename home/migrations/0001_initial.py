# Generated by Django 3.2.7 on 2021-11-06 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('year', models.IntegerField()),
                ('language', models.CharField(max_length=10)),
                ('gener1', models.CharField(max_length=16)),
                ('gener2', models.CharField(max_length=16, null=True)),
                ('duration', models.FloatField(null=True)),
                ('rating', models.FloatField()),
                ('cast1', models.CharField(max_length=64)),
                ('cast2', models.CharField(max_length=64, null=True)),
                ('cast3', models.CharField(max_length=64, null=True)),
                ('director', models.CharField(max_length=64, null=True)),
                ('video', models.CharField(max_length=200, null=True)),
                ('img', models.ImageField(upload_to='media')),
                ('category', models.CharField(max_length=20, null=True)),
                ('imdb_link', models.CharField(max_length=200, null=True)),
                ('story', models.TextField()),
            ],
            options={
                'db_table': 'Movie',
            },
        ),
        migrations.CreateModel(
            name='Banner_Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(upload_to='media')),
                ('story', models.CharField(max_length=150, null=True)),
                ('banner_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.movie')),
            ],
            options={
                'db_table': 'Banner_Movie',
            },
        ),
    ]