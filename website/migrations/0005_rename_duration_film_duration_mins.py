# Generated by Django 5.1.3 on 2024-11-24 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_film_rating_film_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='duration',
            new_name='duration_mins',
        ),
    ]
