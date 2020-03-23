from rest_framework import routers

from assets.views import AssetViewSet

router = routers.DefaultRouter()
router.register(r'assets', AssetViewSet)
