# Generated by Django 2.0.7 on 2018-07-31 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20180731_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmarket',
            name='childtypenames',
            field=models.CharField(max_length=200),
        ),
    ]
