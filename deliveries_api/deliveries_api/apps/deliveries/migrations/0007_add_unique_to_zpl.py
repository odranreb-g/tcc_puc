from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deliveries", "0006_change_away_add_one_to_one_with_zpl"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalzpl",
            name="url",
            field=models.URLField(db_index=True, verbose_name="URL"),
        ),
        migrations.AlterField(
            model_name="zpl",
            name="url",
            field=models.URLField(unique=True, verbose_name="URL"),
        ),
    ]
