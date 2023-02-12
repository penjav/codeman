from django.shortcuts import render


# Create your views here.
def nangchen(request):
    return render(request, "nangchen.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def history(request):
    return render(request, "history.html")


def _base(request):
    return render(request, "_base.html")
