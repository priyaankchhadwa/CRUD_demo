# Generated by Django 2.0.7 on 2018-07-21 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
