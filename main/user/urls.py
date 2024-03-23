from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserDetail







router = DefaultRouter()
router.register("user-detail", UserDetail, basename="user-detail")


urlpatterns = [
   path('', include(router.urls)),
]


