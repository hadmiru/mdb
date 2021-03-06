# Generated by Django 2.0.5 on 2018-06-09 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechdb_core', '0029_auto_20180609_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment_sizename',
            name='type',
            field=models.CharField(choices=[('pump', 'Насос'), ('compressor', 'Компрессор'), ('bench', 'Станок'), ('e-engine', 'Электродвигатель'), ('engine', 'ДВС'), ('turbine', 'Турбина'), ('crane', 'ГПМ'), ('air-handling-unit', 'Вент. установка'), ('air-cooling-unit', 'АВО'), ('heat-exchanger', 'Теплообменник'), ('furnace', 'Печь'), ('safe-valve', 'Клапан предохр.'), ('check-valve', 'Клапан обратный'), ('control-valve', 'Задвижка, клапан реглирующий'), ('other', 'Прочее оборудование')], default='other', max_length=25, verbose_name='Тип оборудования'),
        ),
        migrations.AlterField(
            model_name='equipment_sizename',
            name='manufacturer',
            field=models.CharField(default='н/д', max_length=100, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='equipment_sizename',
            name='supply_provider',
            field=models.CharField(default='н/д', max_length=100, verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='equipment_sizename',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
    ]
