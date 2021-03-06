# Generated by Django 2.2.1 on 2019-05-06 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpeedDetector',
            fields=[
                ('c_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('car_speed', models.IntegerField(default=0)),
                ('speed_limit', models.IntegerField(default=0)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('date_captured', models.DateTimeField(blank=True, null=True)),
                ('car', models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Speed Detector',
                'verbose_name_plural': 'Speed Detector',
                'db_table': 'speed_detector',
            },
        ),
    ]
