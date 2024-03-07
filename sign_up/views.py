from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from typing import Callable, Dict, Any

# Create your views here.

def registration(request: HttpRequest) -> HttpResponse:
    context: Dict[str] = {
        "gay": "gay",
    }
    print(request.POST.get("login"))
    print(request.POST.get("password"))
    return render(request, "base.html", context=context)

