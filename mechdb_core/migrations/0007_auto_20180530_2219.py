# Generated by Django 2.0.5 on 2018-05-30 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechdb_core', '0006_container_is_repair_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='in_container_id',
            field=models.IntegerField(default=0),
        ),
    ]
