# Generated by Django 2.0.7 on 2020-02-14 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20200214_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(max_length=250),
        ),
    ]
