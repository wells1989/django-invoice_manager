# Generated by Django 5.0.4 on 2024-05-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invoice", "0015_invoice_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="tag",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]