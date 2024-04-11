from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()

def handler(request):
    response = app(request)
    return response