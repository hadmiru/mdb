# Generated by Django 2.0.5 on 2018-05-30 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mechdb_core', '0007_auto_20180530_2219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='container',
            old_name='descripton',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='manufacturer',
            old_name='descripton',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='supply_provider',
            old_name='descripton',
            new_name='description',
        ),
    ]