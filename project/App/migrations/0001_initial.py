# Generated by Django 2.0.7 on 2018-07-28 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=36)),
                ('trackid', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axf_wheel',
            },
        ),
    ]
