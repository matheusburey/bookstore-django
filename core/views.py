from django.shortcuts import HttpResponse


# Create your views here.
def teste(request):
    return HttpResponse({"message": "Hello, world. You're at the livraria index."})
