# Generated by Django 3.2 on 2021-10-18 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20211018_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='agent',
            field=models.CharField(default='None', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='budget',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='order',
            name='campus',
            field=models.CharField(default='None', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='furnished',
            field=models.CharField(default='None', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='location',
            field=models.CharField(default='None', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='occupation',
            field=models.CharField(default='None', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='room_size',
            field=models.CharField(default='None', max_length=256),
            preserve_default=False,
        ),
    ]