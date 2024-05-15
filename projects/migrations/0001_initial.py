# Generated by Django 4.1.5 on 2023-03-26 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.division')),
                ('product', models.ForeignKey(db_column='product_name', on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]