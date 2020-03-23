# Generated by Django 3.0.4 on 2020-03-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20200322_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='assetvalue',
            name='settlement_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
