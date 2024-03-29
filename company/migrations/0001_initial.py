# Generated by Django 3.2 on 2021-10-04 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('telephone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('display_picture', models.ImageField(default='company.jpg', upload_to='company/profile/')),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
    ]
