# Generated by Django 3.1.4 on 2020-12-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedata',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]
