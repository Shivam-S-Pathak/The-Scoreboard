# Generated by Django 5.0.1 on 2024-03-01 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_table',
            new_name='student',
        ),
    ]