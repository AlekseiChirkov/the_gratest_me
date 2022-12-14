from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.points import views

router = DefaultRouter()
router.register('', views.ScaleModelViewSet, basename='scale')


urlpatterns = [
    path('', include(router.urls)),
]


