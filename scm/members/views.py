from django.shortcuts import render

# Create your views here.

def sign_up_success(request):
    template = 'members/sign_up_success.html'
    return render(request, template)