from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello worlds, you are at the polls index")