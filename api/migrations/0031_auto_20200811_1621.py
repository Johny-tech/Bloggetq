# Generated by Django 3.0.8 on 2020-08-11 11:21

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20200806_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bannerpic',
            field=models.ImageField(blank=True, default='code_review.jpeg',
                                    null=True, upload_to=api.models.upload_banner_to),
        ),
    ]
