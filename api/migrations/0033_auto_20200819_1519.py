# Generated by Django 3.0.8 on 2020-08-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_auto_20200814_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='posts', to='api.Category'),
        ),
    ]
