from django.urls import path

from community.views import index

app_name = "community"

urlpatterns = [
    path("", index, name="index"),
]
