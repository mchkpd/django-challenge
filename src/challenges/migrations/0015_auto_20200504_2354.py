# Generated by Django 2.2.3 on 2020-05-04 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0014_auto_20200504_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='is_completed',
            field=models.BooleanField(),
        ),
    ]