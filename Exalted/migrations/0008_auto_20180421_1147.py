# Generated by Django 2.0.4 on 2018-04-21 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exalted', '0007_auto_20180421_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requirementset',
            name='charm',
        ),
        migrations.RemoveField(
            model_name='requirementset',
            name='requirement',
        ),
    ]
