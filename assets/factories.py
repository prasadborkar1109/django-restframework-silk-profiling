import factory
from factory import fuzzy
from faker import Factory

from assets.models import AssetType, AssetValue, Asset

faker = Factory.create()


class AssetTypeFactory(factory.DjangoModelFactory):
    class Meta:
        model = AssetType

    asset_type_name = faker.text(max_nb_chars=50)
    asset_type_desc = faker.text(max_nb_chars=200)


class AssetFactory(factory.DjangoModelFactory):
    class Meta:
        model = Asset

    # class Params:
    asset_type_id = factory.SubFactory(AssetTypeFactory)

    asset_name = faker.name()
    asset_description = faker.text(max_nb_chars=200)


class AssetValueFactory(factory.DjangoModelFactory):
    class Meta:
        model = AssetValue

    # class Params:
    asset_id = factory.SubFactory(AssetFactory)

    reporting_date = faker.date()
    opening_price = fuzzy.FuzzyInteger(0)
    settlement_price = fuzzy.FuzzyInteger(0)
    trading_volume = fuzzy.FuzzyInteger(0, high=100)
    currency = fuzzy.FuzzyText(length=5)


