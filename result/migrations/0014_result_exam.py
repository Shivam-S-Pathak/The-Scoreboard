# Generated by Django 5.0.1 on 2024-03-05 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0013_remove_exam_course_remove_result_exam_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='exam',
            field=models.CharField(default='0', max_length=30),
        ),
    ]
