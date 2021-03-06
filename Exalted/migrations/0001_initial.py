# Generated by Django 2.0.4 on 2018-04-20 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='AbilitySet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField()),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Exalted.Ability')),
            ],
        ),
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('rating', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(max_length=90)),
                ('character_essence', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'character',
            },
        ),
        migrations.CreateModel(
            name='Charm',
            fields=[
                ('charm_id', models.IntegerField(primary_key=True, serialize=False)),
                ('charm_name', models.CharField(max_length=90)),
                ('charm_duration', models.CharField(max_length=64)),
                ('charm_cost_motes', models.SmallIntegerField()),
                ('charm_cost_wp', models.SmallIntegerField()),
                ('charm_cost_other', models.CharField(max_length=64)),
                ('charm_essence_min', models.SmallIntegerField()),
                ('charm_no_eclipse', models.BooleanField()),
                ('charm_prayer_strip', models.BooleanField()),
                ('charm_description', models.TextField()),
                ('charm_abilitySet', models.ManyToManyField(to='Exalted.AbilitySet')),
            ],
            options={
                'db_table': 'charm_data',
            },
        ),
        migrations.CreateModel(
            name='Charm_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Exalted_subtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exalted_subtype_name', models.CharField(max_length=64)),
                ('exalted_subtype_eclipse', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Exalted_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exalted_type_id', models.IntegerField()),
                ('exalted_type_name', models.CharField(max_length=64)),
                ('exalted_type_ability_cost', models.SmallIntegerField()),
                ('exalted_type_attribute_cost', models.SmallIntegerField()),
                ('exalted_type_charm_cost', models.SmallIntegerField()),
                ('exalted_type_essence_cost', models.SmallIntegerField()),
                ('exalted_type_extended_charm_cost', models.SmallIntegerField()),
                ('exalted_type_favored_cost', models.SmallIntegerField()),
                ('exalted_type_favored_modifier', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FavoredItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='HealthLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('rating', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HealthLevels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('value', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HealthLevelSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_levels', models.ManyToManyField(to='Exalted.HealthLevel')),
            ],
        ),
        migrations.CreateModel(
            name='KungfuCircle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='MagicCircle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='exalted_type',
            name='exalted_type_available_kungfu',
            field=models.ManyToManyField(related_name='_exalted_type_exalted_type_available_kungfu_+', to='Exalted.KungfuCircle'),
        ),
        migrations.AddField(
            model_name='exalted_type',
            name='exalted_type_available_magic',
            field=models.ManyToManyField(related_name='_exalted_type_exalted_type_available_magic_+', to='Exalted.MagicCircle'),
        ),
        migrations.AddField(
            model_name='exalted_type',
            name='exalted_type_favored_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Exalted.FavoredItems'),
        ),
        migrations.AddField(
            model_name='exalted_type',
            name='exalted_type_health_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Exalted.HealthLevels'),
        ),
        migrations.AddField(
            model_name='exalted_subtype',
            name='exalted_subtype_exalted_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Exalted.Exalted_type'),
        ),
        migrations.AddField(
            model_name='exalted_subtype',
            name='exalted_subtype_health_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Exalted.HealthLevels'),
        ),
        migrations.AddField(
            model_name='charm',
            name='charm_ex_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Exalted.Exalted_type'),
        ),
        migrations.AddField(
            model_name='charm',
            name='charm_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Exalted.Charm_type'),
        ),
        migrations.AddField(
            model_name='character',
            name='character_exalted_subtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Exalted.Exalted_subtype'),
        ),
        migrations.AddField(
            model_name='character',
            name='character_exalted_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Exalted.Exalted_type'),
        ),
        migrations.AddField(
            model_name='character',
            name='character_health_level_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exalted.HealthLevelSet'),
        ),
        migrations.AddField(
            model_name='character',
            name='character_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Exalted.Location'),
        ),
    ]
