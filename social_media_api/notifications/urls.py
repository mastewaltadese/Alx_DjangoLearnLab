from django.urls import path
from .views import user_notifications, mark_notifications_as_read

urlpatterns = [
    path('notifications/', user_notifications, name='user-notifications'),
    path('notifications/mark-read/', mark_notifications_as_read, name='mark-notifications-read'),
]

