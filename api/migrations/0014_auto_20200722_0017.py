# Generated by Django 3.0.8 on 2020-07-21 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_coment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coments', to='api.Post'),
        ),
    ]
