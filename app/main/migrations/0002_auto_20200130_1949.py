# Generated by Django 2.2.9 on 2020-01-30 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]