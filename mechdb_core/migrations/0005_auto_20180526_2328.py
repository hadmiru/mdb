# Generated by Django 2.0.5 on 2018-05-26 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechdb_core', '0004_auto_20180526_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='used_in_equipment',
            field=models.ManyToManyField(to='mechdb_core.Equipment'),
        ),
    ]