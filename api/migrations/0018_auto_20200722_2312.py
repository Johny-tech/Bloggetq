# Generated by Django 3.0.8 on 2020-07-22 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20200722_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='popularity',
        ),
        migrations.RemoveField(
            model_name='post',
            name='stars',
        ),
    ]