# Generated by Django 2.0.5 on 2018-06-08 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechdb_core', '0027_auto_20180608_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='used_in_container',
            field=models.ManyToManyField(related_name='used_in_container', to='mechdb_core.Container'),
        ),
    ]
