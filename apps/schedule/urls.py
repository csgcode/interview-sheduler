from rest_framework.routers import DefaultRouter
from django.urls import include, path

from apps.schedule.api import views

app_name = 'schedule'

# API urls declared here all URL's are prepended with 'api/v1/'
router = DefaultRouter()
router.register(r'available-time', views.AvailableTimeViewSet, basename='available-time')


api_v1_url_patterns = [
    path('', include(router.urls)),
    path('view-available-time/', views.ScheduleView.as_view(), name='schedule-time')
]

