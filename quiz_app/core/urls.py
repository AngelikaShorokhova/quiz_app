from django.urls import include, path

urlpatterns = [
    path('', include('classroom.urls')),
]
