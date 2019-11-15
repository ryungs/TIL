from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def hi(request, names):
    ss32 = [
        'dr',
        'yr',
        'st',
        'dg',
        'jy'
    ]
    return render(request, 'hi.html', {'name': names, 'ss3': ss32})