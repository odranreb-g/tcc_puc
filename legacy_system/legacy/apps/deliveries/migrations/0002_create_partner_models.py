import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deliveries", "0001_create_delivery_models"),
    ]

    operations = [
        migrations.CreateModel(
            name="Partner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="name")),
                (
                    "status",
                    models.CharField(
                        choices=[("ACTIVE", "ACTIVE"), ("INACTIVE", "INACTIVE")],
                        default="ACTIVE",
                        max_length=8,
                        verbose_name="status",
                    ),
                ),
            ],
            options={
                "verbose_name": "Patner",
                "verbose_name_plural": "Patners",
            },
        ),
        migrations.AlterField(
            model_name="delivery",
            name="status",
            field=models.CharField(
                choices=[("IN_TRANSIT", "IN_TRANSIT"), ("DONE", "DONE")],
                default="IN_TRANSIT",
                max_length=10,
                verbose_name="status",
            ),
        ),
        migrations.CreateModel(
            name="PartnerRoute",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("start_place", models.CharField(max_length=10, verbose_name="start_place")),
                ("finish_place", models.CharField(max_length=10, verbose_name="finish_place")),
                ("price", models.DecimalField(decimal_places=2, max_digits=5, verbose_name="price")),
                (
                    "partner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="deliveries.partner"
                    ),
                ),
            ],
            options={
                "verbose_name": "PartnerRoute",
                "verbose_name_plural": "PartnerRoutes",
            },
        ),
    ]
