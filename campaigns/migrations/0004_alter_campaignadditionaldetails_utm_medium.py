# Generated by Django 4.1.5 on 2023-04-25 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0003_alter_campaignadditionaldetails_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignadditionaldetails',
            name='utm_medium',
            field=models.CharField(choices=[('QR', 'QR'), ('Accessible QR', 'Accessible QR'), ('RFID', 'RFID'), ('NFC', 'NFC')], max_length=13),
        ),
    ]
