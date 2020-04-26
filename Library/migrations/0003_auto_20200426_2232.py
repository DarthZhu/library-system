# Generated by Django 3.0.5 on 2020-04-26 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0002_auto_20200423_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbill',
            old_name='income',
            new_name='pay',
        ),
        migrations.RemoveField(
            model_name='adminbill',
            name='outcome',
        ),
        migrations.AddField(
            model_name='adminbill',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adminbill',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
