# Generated by Django 4.2.5 on 2023-09-24 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_yrok_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='spisok',
            name='yrok',
            field=models.ManyToManyField(to='main.yrok'),
        ),
    ]