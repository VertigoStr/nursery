from django.conf import settings
from django.urls import path, include

app_name = 'v1'

urlpatterns = [
    path('child/',
         include('api.v1.child.urls',
                 namespace='child')),
    path('journal/',
         include('api.v1.journal.urls',
                 namespace='journal'))
    ]

if settings.DEBUG:
    from rest_framework_swagger.views import get_swagger_view
    swagger_view = get_swagger_view(
        title='Nursery API v1',
        urlconf='api.v1.urls',
        url='/api/v1/'
    )
    urlpatterns.append(path('swagger/', swagger_view))
