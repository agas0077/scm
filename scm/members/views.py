# Third Party Library
from django.shortcuts import render


def sign_up_success(request):
    template = "members/sign_up_success.html"
    return render(request, template)
