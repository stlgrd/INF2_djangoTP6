# Generated by Django 4.0 on 2021-12-28 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('sim_manager', '0006_remove_simulation_is_favorite_remove_simulation_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
            preserve_default=False,
        ),
    ]
