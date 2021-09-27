from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deliveries", "0003_add_nullable_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="delivery",
            name="type",
            field=models.CharField(
                choices=[("QUOTATION", "QUOTATION"), ("DELIVERY", "DELIVERY")],
                default="QUOTATION",
                max_length=9,
                verbose_name="type",
            ),
        ),
    ]
