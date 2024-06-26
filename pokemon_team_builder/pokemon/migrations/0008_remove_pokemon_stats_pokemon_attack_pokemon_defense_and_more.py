# Generated by Django 5.0.4 on 2024-04-27 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0007_alter_move_accuracy_alter_move_power_alter_move_pp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='stats',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='attack',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='defense',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='hp',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='special_attack',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='special_defense',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='speed',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Stat',
        ),
    ]
