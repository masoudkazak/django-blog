# Generated by Django 3.2.5 on 2021-07-25 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210724_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 25, 10, 37, 49, 831780)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_post',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 25, 10, 37, 49, 831780)),
        ),
    ]
