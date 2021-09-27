from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deliveries", "0002_create_partner_models"),
    ]

    operations = [
        migrations.AlterField(
            model_name="delivery",
            name="delivery_date",
            field=models.DateField(null=True, verbose_name="delivery_date"),
        ),
        migrations.AlterField(
            model_name="delivery",
            name="expected_delivery_date",
            field=models.DateField(verbose_name="expected_delivery_date"),
        ),
        migrations.AlterField(
            model_name="delivery",
            name="receiver_postal_code",
            field=models.CharField(max_length=10, verbose_name="receiver_postal_code"),
        ),
        migrations.AlterField(
            model_name="delivery",
            name="sender_postal_code",
            field=models.CharField(max_length=10, verbose_name="sender_postal_code"),
        ),
    ]
