# Generated by Django 3.0.3 on 2020-02-21 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0006_auto_20200220_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='rank',
            field=models.IntegerField(default=1),
        ),
    ]
