# Generated by Django 2.2.3 on 2020-05-04 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0010_auto_20200504_2343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challenge',
            old_name='activity_id',
            new_name='activity',
        ),
    ]
