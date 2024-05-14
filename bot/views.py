from django.shortcuts import render
from django.http import HttpResponse


def slack_events_endpoint(request):
    return HttpResponse("Hello, world. You're at the slack events endpoint.")
