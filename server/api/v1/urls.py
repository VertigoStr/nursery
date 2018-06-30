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
