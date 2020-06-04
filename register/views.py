from django.shortcuts import render

# Create your views here.
def client(request):
    return render(request, 'register-client.html')

def partner(request):
    return render(request, 'index.html')