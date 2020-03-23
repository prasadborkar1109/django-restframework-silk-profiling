from django.contrib import admin

from assets.models import Asset, AssetType, AssetValue


class AssetAdmin(admin.ModelAdmin):
    list_display = ['id', 'asset_name', 'asset_description', 'asset_type_id']


class AssetTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'asset_type_name', 'asset_type_desc']


class AssetValueAdmin(admin.ModelAdmin):
    list_display = ['id', 'asset_id', 'reporting_date', 'opening_price', 'currency']


admin.site.register(Asset, AssetAdmin)
admin.site.register(AssetType, AssetTypeAdmin)
admin.site.register(AssetValue, AssetValueAdmin)
