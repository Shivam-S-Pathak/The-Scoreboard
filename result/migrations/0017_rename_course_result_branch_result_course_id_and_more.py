# Generated by Django 5.0.1 on 2024-03-05 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0016_rename_result_result_res'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='course',
            new_name='Branch',
        ),
        migrations.AddField(
            model_name='result',
            name='course_id',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='result',
            name='course_name',
            field=models.CharField(default='0', max_length=30),
        ),
    ]
