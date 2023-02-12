from django.shortcuts import render


# Create your views here.
def nangchen(request):
    return render(request, "nangchen.html")


def about(request):
    return render(request, "about.html")
