# Generated by Django 3.2.16 on 2022-10-19 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2002-05-23'),
            preserve_default=False,
        ),
    ]
