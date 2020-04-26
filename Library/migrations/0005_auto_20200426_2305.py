# Generated by Django 3.0.5 on 2020-04-26 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0004_auto_20200426_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminbill',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.Book'),
        ),
        migrations.AlterField(
            model_name='userbill',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.Book'),
        ),
    ]