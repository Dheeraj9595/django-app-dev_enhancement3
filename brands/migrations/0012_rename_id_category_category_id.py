# Generated by Django 4.1.5 on 2024-04-22 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("brands", "0011_rename_category_id_category_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="id",
            new_name="category_id",
        ),
    ]