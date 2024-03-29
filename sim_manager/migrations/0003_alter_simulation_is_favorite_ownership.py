# Generated by Django 4.0 on 2021-12-28 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('sim_manager', '0002_simulation_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulation',
            name='is_favorite',
            field=models.BooleanField(default=0),
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_owner', models.BooleanField(default=1)),
                ('is_favorite', models.BooleanField(default=0)),
                ('simulation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sim_manager.simulation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.user')),
            ],
        ),
    ]
