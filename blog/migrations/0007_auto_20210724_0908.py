# Generated by Django 3.2.5 on 2021-07-24 04:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210724_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 24, 9, 8, 39, 71269)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_post',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 24, 9, 8, 39, 71269)),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
