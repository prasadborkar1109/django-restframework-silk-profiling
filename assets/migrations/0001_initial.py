# Generated by Django 3.0.4 on 2020-03-21 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(max_length=50)),
                ('asset_description', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_type_name', models.CharField(max_length=50)),
                ('asset_type_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AssetValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporting_date', models.DateTimeField()),
                ('opening_price', models.PositiveIntegerField()),
                ('settlement_price', models.PositiveIntegerField()),
                ('trading_volume', models.PositiveIntegerField()),
                ('asset_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Asset')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.AssetType'),
        ),
    ]