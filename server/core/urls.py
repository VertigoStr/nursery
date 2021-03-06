import os

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
]

if settings.DEBUG:

    urlpatterns += [
        path('', TemplateView.as_view(template_name='base.html'), name='base'),
    ]

    from rest_framework_swagger.views import get_swagger_view
    urlpatterns.append(path('api/', get_swagger_view('Nursery API')))

    if int(os.getenv('ENABLE_DEBUG_TOOLBAR', 0)):
        import debug_toolbar

        urlpatterns = [
            path(r'__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
