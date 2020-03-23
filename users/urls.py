from rest_framework import routers

from users.views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)
