# Generated by Django 5.0.2 on 2024-04-24 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_alter_book_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('genre', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
