# Generated by Django 3.2 on 2021-10-20 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20211018_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='agent',
            new_name='agency',
        ),
    ]
