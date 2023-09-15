# Generated by Django 4.2.2 on 2023-06-07 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Position",
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
                ("Name", models.CharField(max_length=100, null=True)),
                ("Area", models.CharField(max_length=100, null=True)),
                ("Road", models.CharField(max_length=100, null=True)),
                ("Door_num", models.CharField(max_length=100, null=True)),
                ("Floor", models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
