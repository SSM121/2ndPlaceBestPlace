from django.db import migrations
from django.utils import timezone

# test for events page. remove before production. potetntial security flaw given default account info
def populate_db(apps, schema_editor):
    Event = apps.get_model('parkingGenie', 'Event')

    e1 = Event(
        name = "San Diego State at Utah State",
        shortName = "SDSUatUSU",
        date= timezone.now(),
        address= '875 Douglas Dr, Logan, UT 84321',
    )
    e1.save()
    e2 = Event(
        name = "Idaho State at Utah State",
        shortName = "ISUatUSU",
        date= timezone.now(),
        address= '875 Douglas Dr, Logan, UT 84321',
    )
    e2.save()
    Lot = apps.get_model('parkingGenie', 'ParkingLot')
    l1 = Lot(
        name = "Spectrum 1",
        address = "900 E 900 N, Logan, UT 84322",
        parking = 20,
        tailgate = 0,
        date = e1.date,
        price = 20,
        tailgatePrice = 0
    )
    l1.save()
    l1.event.add(e1)
    l2 = Lot(
        name = "Spectrum 2",
        address = "900 E 900 N, Logan, UT 84322",
        parking = 7,
        tailgate = 2,
        date = e1.date,
        price = 25,
        tailgatePrice = 60
    )
    l2.save()
    l2.event.add(e1)
    l3 = Lot(
        name = "Spectrum 3",
        address = "900 E 900 N, Logan, UT 84322",
        parking = 214,
        tailgate = 0,
        date = e1.date,
        price = 30,
        tailgatePrice = 0
    )
    l3.save()
    l3.event.add(e1)
    l4 = Lot(
        name = "Spectrum 4",
        address = "900 E 900 N, Logan, UT 84322",
        parking = 25,
        tailgate = 56,
        date = e1.date,
        price = 40,
        tailgatePrice = 100
    )
    l4.save()
    l4.event.add(e1)
    l4.event.add(e2)



class Migration(migrations.Migration):

    dependencies = [
        ('parkingGenie', '0003_qrcodes'),
    ]

    operations = [
            migrations.RunPython(populate_db)
    ]

