from django.db import models


class AssetType(models.Model):
    asset_type_name = models.CharField(max_length=50)
    asset_type_desc = models.CharField(max_length=200)

    def __str__(self):
        return self.asset_type_name


class Asset(models.Model):
    asset_name = models.CharField(max_length=50)
    asset_description = models.CharField(max_length=200, null=True, blank=True)
    asset_type_id = models.ForeignKey(AssetType, on_delete=models.CASCADE)

    def __str__(self):
        return self.asset_name


class AssetValue(models.Model):
    asset_id = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='assets')
    reporting_date = models.DateTimeField()
    opening_price = models.PositiveIntegerField()
    settlement_price = models.PositiveIntegerField(null=True, blank=True)
    trading_volume = models.PositiveIntegerField()
    currency = models.CharField(max_length=5, default='INR')

    def __str__(self):
        return str(self.asset_id)
