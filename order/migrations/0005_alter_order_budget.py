# Generated by Django 3.2 on 2021-11-03 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_rename_agent_order_agency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='budget',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
