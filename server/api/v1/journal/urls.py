from rest_framework import routers

from api.v1.journal.views import JournalViewSet

app_name = 'journal'

router = routers.DefaultRouter()
router.register('journal', JournalViewSet, base_name='journal')

urlpatterns = router.urls
