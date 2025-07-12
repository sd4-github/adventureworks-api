from django.urls import path,include
from rest_framework import routers
from .views import PersonViewset

router = routers.DefaultRouter()
router.register(r'person', PersonViewset)

urlpatterns = [
    path('', include(router.urls)),
]
