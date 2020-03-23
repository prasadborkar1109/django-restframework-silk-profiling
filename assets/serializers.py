from rest_framework import serializers

from assets.models import Asset, AssetValue


class AssetValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetValue
        fields = ['id', 'asset_id', 'reporting_date', 'opening_price', 'currency']


class AssetSerializer(serializers.ModelSerializer):
    value_history = serializers.SerializerMethodField()

    class QueryParamSerializer(serializers.Serializer):
        asset_type_id = serializers.ListField(required=False, child=serializers.IntegerField())
        opening_price_min = serializers.IntegerField(required=False)
        opening_price_max = serializers.IntegerField(required=False)

    class Meta:
        model = Asset
        fields = ['id', 'asset_name', 'asset_description', 'asset_type_id', 'value_history']

    def get_value_history(self, obj):
        value_data = AssetValue.objects.filter(asset_id=obj.id)
        return AssetValueSerializer(value_data, many=True).data

    param_errors = []
    param_serializer = QueryParamSerializer
