# Generated by Django 4.0 on 2021-12-28 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('sim_manager', '0018_alter_simulation_user_shared'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulation',
            name='user_shared',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_shared', to='auth.user'),
        ),
    ]
