from django.db import migrations
from django.utils import timezone

# test for events page. remove before production. potetntial security flaw given default account info
def populate_db(apps, schema_editor):
    Account = apps.get_model('parkingGenie', 'Account')
    Manager = apps.get_model('parkingGenie', 'Manager')
    Event = apps.get_model('parkingGenie', 'Event')
    a = Account(userType = 3, name="Default Manager", email="manager@manager.net", password="1234")
    a.save()
    m = Manager(user=a)
    m.save()
    e1 = Event(
        name = "San Diego State at Utah State",
        shortName = "SDSUatUSU",
        date= timezone.now(),
        address= '875 Douglas Dr, Logan, UT 84321',
        manager = m
    )
    e1.save()
    e2 = Event(
        name = "Idaho State at Utah State",
        shortName = "ISUatUSU",
        date= timezone.now(),
        address= '875 Douglas Dr, Logan, UT 84321',
        manager = m
    )
    e2.save()


class Migration(migrations.Migration):

    dependencies = [
        ('parkingGenie', '0011_event_date'),
    ]

    operations = [
            migrations.RunPython(populate_db)
    ]

