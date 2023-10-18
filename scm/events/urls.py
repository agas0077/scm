from django.urls import path

from events.views import sign_up, index, Gallery

app_name = "events"

urlpatterns = [
    path("sign_up/", sign_up, name="sign_up"),
    path("index/", index, name="index"),
    path("gallery/", Gallery.as_view(), name="gallery"),
]
