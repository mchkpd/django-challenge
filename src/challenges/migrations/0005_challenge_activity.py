# Generated by Django 2.2.3 on 2020-05-04 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0004_remove_activity_minutes'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='challenges.Activity'),
        ),
    ]
