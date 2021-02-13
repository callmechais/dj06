from django.shortcuts import render

# Create your views here.
def sugr(request):
    info = {"key":"plant"}
    return render(request, 'sugr.html', info)