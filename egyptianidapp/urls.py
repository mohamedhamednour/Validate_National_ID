from django.urls import path, include
from rest_framework import routers
from .views import NationalIDViewSet , ValidateNationalIDAPIView

router = routers.DefaultRouter()
router.register('v1/national-id', NationalIDViewSet, basename='v1-national-id')

urlpatterns = [
    path('', include(router.urls)),
    path('v2/national-id/', ValidateNationalIDAPIView.as_view(), name='v2-national-id'),

]
