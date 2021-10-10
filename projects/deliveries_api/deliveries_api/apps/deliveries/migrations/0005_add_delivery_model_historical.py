import uuid

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("deliveries", "0004_add_zpl_model_with_historical_records"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalDelivery",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                ("id", models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ("sender_name", models.CharField(max_length=100, verbose_name="sender_name")),
                ("sender_address", models.CharField(max_length=100, verbose_name="sender_address")),
                ("sender_city", models.CharField(max_length=50, verbose_name="sender_city")),
                ("sender_postal_code", models.CharField(max_length=10, verbose_name="sender_postal_code")),
                ("receiver_name", models.CharField(max_length=100, verbose_name="receiver_name")),
                ("receiver_address", models.CharField(max_length=100, verbose_name="receiver_address")),
                ("receiver_city", models.CharField(max_length=50, verbose_name="receiver_city")),
                (
                    "receiver_postal_code",
                    models.CharField(max_length=10, verbose_name="receiver_postal_code"),
                ),
                (
                    "freight_price",
                    models.DecimalField(decimal_places=2, max_digits=5, verbose_name="freight_price"),
                ),
                ("expected_delivery_date", models.DateField(verbose_name="expected_delivery_date")),
                ("delivery_date", models.DateField(null=True, verbose_name="delivery_date")),
                ("delivery_entry_created", models.DateTimeField()),
                ("delivery_entry_modified", models.DateTimeField()),
                (
                    "type",
                    models.CharField(
                        choices=[("QUOTATION", "QUOTATION"), ("DELIVERY", "DELIVERY")],
                        default="QUOTATION",
                        max_length=9,
                        verbose_name="type",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("QUOTATION", "QUOTATION"), ("IN_TRANSIT", "IN_TRANSIT"), ("DONE", "DONE")],
                        default="QUOTATION",
                        max_length=10,
                        verbose_name="status",
                    ),
                ),
                ("partner_id", models.UUIDField(null=True)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Delivery",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
