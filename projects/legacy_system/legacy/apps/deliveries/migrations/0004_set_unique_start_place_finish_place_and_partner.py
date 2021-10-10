from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("deliveries", "0003_set_freight_price_nullable"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="partnerroute",
            unique_together={("start_place", "finish_place", "partner_id")},
        ),
    ]
