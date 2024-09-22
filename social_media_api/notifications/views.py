from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_notifications(request):
    notifications = request.user.notifications.filter(unread=True)
    data = [{
        'actor': notification.actor.username,
        'verb': notification.verb,
        'target': str(notification.target),
        'timestamp': notification.timestamp
    } for notification in notifications]
    return Response(data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_notifications_as_read(request):
    notifications = request.user.notifications.filter(unread=True)
    notifications.update(unread=False)
    return Response({"detail": "Notifications marked as read."}, status=200)

