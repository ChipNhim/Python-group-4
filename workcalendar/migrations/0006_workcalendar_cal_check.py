# Generated by Django 3.2.8 on 2021-12-01 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workcalendar', '0005_alter_workcalendar_assign'),
    ]

    operations = [
        migrations.AddField(
            model_name='workcalendar',
            name='cal_check',
            field=models.SmallIntegerField(choices=[(0, 'Not yet'), (1, 'Done')], null=True),
        ),
    ]