# Generated by Django 3.1.5 on 2021-04-01 18:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('parkingGenie', '0002_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.UUIDField(default=uuid.UUID('73377ef4-9466-4299-acd3-46cc195d43ab'), help_text='Unique ID for this particular Account', primary_key=True, serialize=False),
        ),
    ]