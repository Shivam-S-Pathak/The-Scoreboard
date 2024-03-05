# Generated by Django 5.0.1 on 2024-03-04 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0007_delete_course_delete_examtype_delete_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exam_type', models.CharField(max_length=30)),
                ('semester', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.course')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('marks', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='examResult',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='course',
            new_name='enrollment_id',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='exam',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
        migrations.AddField(
            model_name='result',
            name='Student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.student'),
        ),
        migrations.AddField(
            model_name='result',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.exam'),
        ),
    ]