# Generated by Django 2.0.4 on 2018-04-21 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Exalted', '0008_auto_20180421_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirementset',
            name='charm',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='requirementset', to='Exalted.Charm'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requirementset',
            name='requirement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='requirementset', to='Exalted.Requirement'),
        ),
    ]
