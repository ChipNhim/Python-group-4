# Generated by Django 3.2.8 on 2021-12-01 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workcalendar', '0004_merge_0003_auto_20211127_0329_0003_auto_20211127_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workcalendar',
            name='assign',
            field=models.TextField(),
        ),
    ]
