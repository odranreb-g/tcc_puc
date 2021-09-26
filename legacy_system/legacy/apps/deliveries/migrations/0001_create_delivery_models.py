import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Delivery",
            fields=[
                ("start", models.DateTimeField(blank=True, null=True, verbose_name="start")),
                ("end", models.DateTimeField(blank=True, null=True, verbose_name="end")),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
                ),
                ("sender_name", models.CharField(max_length=100, verbose_name="sender_name")),
                ("sender_address", models.CharField(max_length=100, verbose_name="sender_address")),
                ("sender_city", models.CharField(max_length=50, verbose_name="sender_city")),
                ("sender_postal_code", models.CharField(max_length=10, verbose_name="sender_city")),
                ("receiver_name", models.CharField(max_length=100, verbose_name="receiver_name")),
                ("receiver_address", models.CharField(max_length=100, verbose_name="receiver_address")),
                ("receiver_city", models.CharField(max_length=50, verbose_name="receiver_city")),
                ("receiver_postal_code", models.CharField(max_length=10, verbose_name="receiver_city")),
                (
                    "freight_price",
                    models.DecimalField(decimal_places=2, max_digits=5, verbose_name="freight_price"),
                ),
                ("expected_delivery_date", models.DateTimeField(verbose_name="expected_delivery_date")),
                ("delivery_date", models.DateTimeField(verbose_name="delivery_date")),
                (
                    "status",
                    models.CharField(
                        choices=[("IN_TRANSIT", "IN_TRANSIT"), ("DONE", "DONE")],
                        default="IN_TRANSIT",
                        max_length=50,
                        verbose_name="status",
                    ),
                ),
            ],
            options={
                "verbose_name": "Delivery",
                "verbose_name_plural": "Deliveries",
            },
        ),
    ]
