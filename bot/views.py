from django.http import HttpResponse


def slack_events_endpoint(request):
    return HttpResponse("<h1>Hello world</h1>", status=200)
