# Generated by Django 4.1.5 on 2023-06-06 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0008_alter_campaignadditionaldetails_utm_medium'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaignadditionaldetails',
            old_name='utm_term',
            new_name='variant',
        ),
        migrations.RemoveField(
            model_name='campaignadditionaldetails',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='campaignadditionaldetails',
            name='market',
        ),
        migrations.RemoveField(
            model_name='campaignadditionaldetails',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='campaignadditionaldetails',
            name='utm_medium',
        ),
        migrations.RemoveField(
            model_name='campaignadditionaldetails',
            name='utm_source',
        ),
        migrations.AlterField(
            model_name='campaignadditionaldetails',
            name='code_placement',
            field=models.CharField(choices=[('PackPrimary', 'PackPrimary'), ('PackSecondary', 'PackSecondary'), ('PackSamples', 'PackSamples'), ('Stickers', 'Stickers'), ('OOH', 'OOH'), ('DOOH', 'DOOH'), ('POS', 'POS'), ('PrintMedia', 'PrintMedia'), ('TV', 'TV'), ('Insert', 'Insert'), ('DirectMail', 'DirectMail'), ('DeliveryBox', 'DeliveryBox'), ('Leaflet', 'Leaflet'), ('OnlineVideo', 'OnlineVideo')], max_length=100),
        ),
    ]
