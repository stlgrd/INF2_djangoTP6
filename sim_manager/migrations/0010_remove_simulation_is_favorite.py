# Generated by Django 4.0 on 2021-12-28 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sim_manager', '0009_simulation_is_favorite_simulation_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simulation',
            name='is_favorite',
        ),
    ]