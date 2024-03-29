# Generated by Django 4.2.5 on 2023-10-04 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SupportRequests",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("DOB", models.DateField()),
                ("email", models.EmailField(max_length=254)),
                ("ip", models.CharField(max_length=30)),
                ("description", models.TextField()),
            ],
            options={
                "db_table": "support_requests",
            },
        ),
    ]
