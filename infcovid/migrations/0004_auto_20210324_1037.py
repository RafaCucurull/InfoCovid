# Generated by Django 3.1.7 on 2021-03-24 10:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('infcovid', '0003_auto_20210320_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 24, 10, 37, 34, 116378, tzinfo=utc)),
        ),
    ]