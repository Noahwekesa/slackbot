from django.urls import path
from bot import views


urlpatterns = [
    path("events/", views.slack_events_endpoint),
]
