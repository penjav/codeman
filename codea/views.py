from django.shortcuts import render
import datetime


# Create your views here.
def nangchen(request):
    losar = datetime.datetime.now()
    return render(
        request,
        "nangchen.html",
        {
            "losar": losar.month == 2 and losar.day == 20,
        },
    )


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def history(request):
    return render(request, "history.html")


def _base(request):
    lo = datetime.datetime.now()
    return render(request, "_base.html", {"newyear": True})
