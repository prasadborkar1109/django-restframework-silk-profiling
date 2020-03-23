from django.test import TestCase, Client
from django.urls.base import reverse

from assets.models import Asset, AssetValue, AssetType
from assets.factories import AssetFactory, AssetTypeFactory, AssetValueFactory


class AssetEndpointTest(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.asset_type = AssetTypeFactory()
        self.asset = AssetFactory(asset_type_id=self.asset_type)
        self.asset_value = AssetValueFactory(asset_id=self.asset)

    def _asset_url(self):
        return reverse('asset-list')

    def test_get_asset_data(self):
        url = self._asset_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]['asset_name'], self.asset.asset_name)
        self.assertEqual(response.data['results'][0]['asset_type_id'], self.asset_type.id)


