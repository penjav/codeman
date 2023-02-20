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
    losar = datetime.datetime.now()
    return render(
        request,
        "about.html",
        {
            "losar": losar.month == 2 and losar.day == 20,
        },
    )


def contact(request):
    losar = datetime.datetime.now()
    return render(
        request,
        "contact.html",
        {
            "losar": losar.month == 2 and losar.day == 20,
        },
    )


def history(request):
    losar = datetime.datetime.now()
    return render(
        request,
        "history.html",
        {
            "losar": losar.month == 2 and losar.day == 20,
        },
    )


def _base(request):
    losar = datetime.datetime.now()
    return render(
        request,
        "_base.html",
        {
            "losar": losar.month == 2 and losar.day == 20,
            "losar": losar.month == 2 and losar.day == 21,
            "losar": losar.month == 2 and losar.day == 22,
            "losar": losar.month == 2 and losar.day == 22,
        },
    )
