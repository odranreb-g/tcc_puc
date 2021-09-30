from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deliveries", "0006_fix_wrong_models"),
    ]

    operations = [
        migrations.AlterField(
            model_name="delivery",
            name="status",
            field=models.CharField(
                choices=[("QUOTATION", "QUOTATION"), ("IN_TRANSIT", "IN_TRANSIT"), ("DONE", "DONE")],
                default="QUOTATION",
                max_length=10,
                verbose_name="status",
            ),
        ),
    ]
