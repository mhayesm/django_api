# Generated by Django 4.0.4 on 2022-04-29 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_rename_movies_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='release_year',
            field=models.PositiveIntegerField(default=2022),
        ),
    ]
