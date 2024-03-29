# Generated by Django 4.0 on 2021-12-29 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('sim_manager', '0020_simulation_is_shared'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simulation',
            name='user_shared',
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simulation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sim_manager.simulation')),
                ('user_shared', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='auth.user')),
            ],
        ),
    ]
