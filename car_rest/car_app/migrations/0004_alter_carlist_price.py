# Generated by Django 5.1.4 on 2024-12-14 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0003_alter_carlist_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carlist',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
