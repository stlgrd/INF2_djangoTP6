# Generated by Django 4.0 on 2021-12-28 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('sim_manager', '0004_user_simulation_delete_ownership'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Simulation',
            new_name='Ownership',
        ),
    ]
