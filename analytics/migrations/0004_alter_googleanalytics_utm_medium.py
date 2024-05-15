# Generated by Django 4.1.5 on 2023-05-13 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_remove_googleanalytics_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googleanalytics',
            name='utm_medium',
            field=models.CharField(choices=[('QR', 'QR'), ('AQR', 'AQR'), ('RFID', 'RFID'), ('NFC', 'NFC')], max_length=13),
        ),
    ]