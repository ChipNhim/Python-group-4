# Generated by Django 3.1 on 2021-11-27 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workcalendar', '0002_room_vehicle_workcalendar'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='check',
            field=models.SmallIntegerField(choices=[(0, 'Chua duyet'), (1, 'Da duyet')], null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='plan',
            field=models.SmallIntegerField(choices=[(0, 'Ke hoach'), (1, 'Dot xuat')], null=True),
        ),
    ]