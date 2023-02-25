from django.shortcuts import render
import datetime


# Create your views here.
def nangchen(request):
    losar = datetime.datetime.now()
    return render(
        request,
        "nangchen.html",
        {
            "losar": losar.month == 2 and losar.day == 25,
        },
    )


def about(request):
    losar = datetime.datetime.now()
    return render(
        request,
        "about.html",
        {
            "losar": losar.month == 2 and losar.day == 25,
        },
    )


def contact(request):
    losar = datetime.datetime.now()
    return render(
        request,
        "contact.html",
        {
            "losar": losar.month == 2 and losar.day == 25,
        },
    )


def history(request):
    losar = datetime.datetime.now()
    return render(
        request,
        "history.html",
        {
            "losar": losar.month == 2 and losar.day == 25,
        },
    )


def _base(request):
    losar = datetime.datetime.now()
    return render(
        request,
        "_base.html",
        {
            "losar": losar.month == 2 and losar.day == 25,
        },
    )
