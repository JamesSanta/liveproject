# Generated by Django 2.2.5 on 2023-09-09 02:13

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Star_Wars', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='character',
            managers=[
                ('Characters', django.db.models.manager.Manager()),
            ],
        ),
    ]
