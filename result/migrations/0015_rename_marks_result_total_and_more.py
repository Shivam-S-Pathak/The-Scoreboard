# Generated by Django 5.0.1 on 2024-03-05 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0014_result_exam'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='marks',
            new_name='Total',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='subject',
            new_name='marks1',
        ),
        migrations.AddField(
            model_name='result',
            name='marks2',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='result',
            name='marks3',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='result',
            name='marks4',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='result',
            name='marks5',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='result',
            name='result',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='result',
            name='subject1',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='result',
            name='subject2',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='result',
            name='subject3',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='result',
            name='subject4',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='result',
            name='subject5',
            field=models.CharField(default='0', max_length=30),
        ),
    ]
