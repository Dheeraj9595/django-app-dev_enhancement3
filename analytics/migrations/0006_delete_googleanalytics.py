# Generated by Django 4.1.5 on 2023-06-06 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_alter_googleanalytics_utm_medium'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GoogleAnalytics',
        ),
    ]