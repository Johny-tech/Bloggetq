# Generated by Django 3.0.8 on 2020-07-23 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20200723_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='api.Coment'),
        ),
    ]
