# Generated by Django 3.1.7 on 2021-03-13 10:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('infcovid', '0003_auto_20210312_1910'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PreguntesTest',
            new_name='PreguntaTest',
        ),
        migrations.AlterField(
            model_name='test',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 13, 10, 46, 14, 214750, tzinfo=utc)),
        ),
    ]
