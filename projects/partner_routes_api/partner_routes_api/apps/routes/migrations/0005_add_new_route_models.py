# Generated by Django 3.2.7 on 2021-10-02 20:16

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0004_add_route_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewRouteCreatedByPartner',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='price')),
                ('start_place', models.CharField(max_length=50, verbose_name='start_place')),
                ('finish_place', models.CharField(max_length=50, verbose_name='finish_place')),
                ('partner_id', models.UUIDField()),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=10, verbose_name='status')),
            ],
            options={
                'verbose_name': 'NewRouteCreatedByPartner',
                'verbose_name_plural': 'NewRoutesCreatedByPartner',
                'unique_together': {('start_place', 'finish_place', 'partner_id')},
            },
        ),
    ]
