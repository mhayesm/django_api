# Generated by Django 4.0.4 on 2022-04-29 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_rename_hero_movies_rename_alias_movies_director'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
    ]