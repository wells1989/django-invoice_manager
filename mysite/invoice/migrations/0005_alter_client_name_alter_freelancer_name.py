# Generated by Django 5.0.4 on 2024-05-09 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invoice", "0004_alter_client_contact_alter_freelancer_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="name",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="freelancer",
            name="name",
            field=models.CharField(max_length=20),
        ),
    ]
