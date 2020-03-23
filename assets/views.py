from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend

from assets.serializers import AssetSerializer
from assets.models import Asset


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='Get List of Assets',
                                                             query_serializer=AssetSerializer.param_serializer))
class AssetViewSet(viewsets.ModelViewSet):

    # Add validation of inputs is_valid()
    # add filters

    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    param_serializer = AssetSerializer.param_serializer
    filter_backends = [DjangoFilterBackend]

    def _validate_query_params(self, query_params):
        serializer = self.get_serializer(data=query_params)
        serializer.is_valid(raise_exception=True)

    def get_queryset(self):
        query_params = self.request.query_params
        param_dict = {'asset_type_id': 'asset_type_id__in', 'opening_price_min': 'assets__opening_price__gte',
                      'opening_price_max': 'assets__opening_price__lte'}
        filters = {}
        for key, value in query_params.items():
            if key in param_dict:
                if key == 'asset_type_id':
                    filters[param_dict.get(key)] = value.split(',')
                else:
                    filters[param_dict.get(key)] = value

        return self.queryset.prefetch_related('assets').filter(**filters)


