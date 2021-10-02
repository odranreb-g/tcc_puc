# Generated by Django 3.2.7 on 2021-10-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0008_change_to_partner_route_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='freight_price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='freight_price'),
        ),
        migrations.AlterField(
            model_name='historicaldelivery',
            name='freight_price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='freight_price'),
        ),
    ]
