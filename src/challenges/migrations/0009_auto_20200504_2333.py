# Generated by Django 2.2.3 on 2020-05-04 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0008_auto_20200504_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='tags',
            field=models.ManyToManyField(blank=True, to='challenges.Tag'),
        ),
    ]
