# Generated by Django 3.1.7 on 2021-03-12 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210311_0924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='city',
            new_name='ciutat',
        ),
        migrations.AddField(
            model_name='customuser',
            name='edat',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='nom',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='sexe',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
