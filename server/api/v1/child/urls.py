from rest_framework import routers

from api.v1.child.views import ChildViewSet, ParentViewSet

app_name = 'child'

router = routers.DefaultRouter()
router.register('child', ChildViewSet, base_name='child')
router.register('parent', ParentViewSet, base_name='parent')

urlpatterns = router.urls
