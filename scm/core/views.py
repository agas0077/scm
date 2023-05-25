from django.shortcuts import render

# Create your views here.

def policy(request):
    template = 'core/policy.html'
    return render(request, template)