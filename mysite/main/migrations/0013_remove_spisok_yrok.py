# Generated by Django 4.2.5 on 2023-09-24 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_spisok_yrok'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spisok',
            name='yrok',
        ),
    ]
