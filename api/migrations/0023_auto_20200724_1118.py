# Generated by Django 3.0.8 on 2020-07-24 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20200723_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsratting',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ratings', to='api.Post'),
        ),
    ]
