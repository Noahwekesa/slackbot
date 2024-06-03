from django.urls import path
from bot import views

app_name = "bot"

urlpatterns = [
    path("events/", views.slack_events_endpoint),
]
