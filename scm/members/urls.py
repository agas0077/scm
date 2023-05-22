from django.urls import path

from members.views import sign_up_success

app_name = 'members'

urlpatterns = [
    path('sign_up_success/', sign_up_success, name='sign_up_success')
]
