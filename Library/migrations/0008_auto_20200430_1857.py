# Generated by Django 3.0.5 on 2020-04-30 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0007_adminbill_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_password',
            field=models.CharField(max_length=100),
        ),
    ]