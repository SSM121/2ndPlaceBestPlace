# Generated by Django 3.1.7 on 2021-03-24 03:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('parkingGenie', '0004_auto_20210322_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4955f08f-9912-4673-b157-42eae1a45136'), help_text='Unique ID for this particular Account', primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='ParkingLot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the parking lot', max_length=20)),
                ('address', models.CharField(help_text='Address of the parking lot', max_length=100)),
                ('parking', models.IntegerField(help_text='Number of available normal parking spaces')),
                ('tailgate', models.IntegerField(help_text='Number of available tailgate parking spaces')),
                ('date', models.DateField(help_text='Date of the Event')),
                ('owner', models.ForeignKey(help_text='Owner of the parking lot', on_delete=django.db.models.deletion.CASCADE, to='parkingGenie.account')),
            ],
        ),
    ]