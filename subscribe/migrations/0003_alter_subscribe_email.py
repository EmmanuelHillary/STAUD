# Generated by Django 3.2 on 2021-11-05 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0002_auto_20211105_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
