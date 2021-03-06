# Generated by Django 3.2.7 on 2021-10-02 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0010_add_new_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='status',
            field=models.CharField(choices=[('QUOTATION', 'QUOTATION'), ('IN_TRANSIT', 'IN_TRANSIT'), ('PLP_PROCESS', 'PLP_PROCESS'), ('ANOTHER_PROCESS', 'ANOTHER_PROCESS'), ('DONE', 'DONE')], default='QUOTATION', max_length=15, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='historicaldelivery',
            name='status',
            field=models.CharField(choices=[('QUOTATION', 'QUOTATION'), ('IN_TRANSIT', 'IN_TRANSIT'), ('PLP_PROCESS', 'PLP_PROCESS'), ('ANOTHER_PROCESS', 'ANOTHER_PROCESS'), ('DONE', 'DONE')], default='QUOTATION', max_length=15, verbose_name='status'),
        ),
    ]
