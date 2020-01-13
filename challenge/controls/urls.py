"""
Controls URLs
"""

from django.urls import path, include
from rest_framework import routers
from .views import ControlView

router = routers.DefaultRouter()
router.register('controls', ControlView)

urlpatterns = [
	path('', include(router.urls))
]