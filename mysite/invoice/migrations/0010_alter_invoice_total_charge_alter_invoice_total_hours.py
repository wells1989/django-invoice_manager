# Generated by Django 5.0.4 on 2024-05-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invoice", "0009_remove_invoice_recurring_alter_invoice_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="total_charge",
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="total_hours",
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
