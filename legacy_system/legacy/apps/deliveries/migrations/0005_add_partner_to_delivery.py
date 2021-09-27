import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deliveries", "0004_add_delivery_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="delivery",
            name="partner",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.DO_NOTHING, to="deliveries.partner"
            ),
        ),
    ]
