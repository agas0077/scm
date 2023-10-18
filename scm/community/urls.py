# Third Party Library
from community.views import index
from django.urls import path

app_name = "community"

urlpatterns = [
    path("", index, name="index"),
]
