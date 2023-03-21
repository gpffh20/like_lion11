from django.shortcuts import render

# if request show 'home.html'
def home(request):
    return render(request, "home.html")

def base(request):
    return render(request, "base.html")