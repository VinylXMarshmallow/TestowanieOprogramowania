# Generated by Django 5.0.2 on 2024-04-24 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_music_popular'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publish_date',
            new_name='published_date',
        ),
        migrations.AlterModelTable(
            name='book',
            table=None,
        ),
    ]
