import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deliveries", "0005_add_delivery_model_historical"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicalzpl",
            name="delivery",
        ),
        migrations.RemoveField(
            model_name="zpl",
            name="delivery",
        ),
        migrations.AddField(
            model_name="delivery",
            name="zpl",
            field=models.OneToOneField(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="deliveries.zpl"
            ),
        ),
        migrations.AddField(
            model_name="historicaldelivery",
            name="zpl",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="deliveries.zpl",
            ),
        ),
    ]
