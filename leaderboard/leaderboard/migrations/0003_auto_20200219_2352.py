# Generated by Django 3.0.3 on 2020-02-19 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0002_remove_agent_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gameID',
            field=models.CharField(max_length=100),
        ),
    ]
