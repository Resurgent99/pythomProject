# Generated by Django 4.2.5 on 2023-09-24 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Yrok',
        ),
    ]
