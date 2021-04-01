# Generated by Django 3.1.5 on 2021-03-24 23:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('parkingGenie', '0004_auto_20210322_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.UUIDField(default=uuid.UUID('573286fa-9d2f-48cb-b1fa-868746677e7a'), help_text='Unique ID for this particular Account', primary_key=True, serialize=False),
        ),
    ]
