from django.urls import path

from core.views import policy

app_name = "core"

urlpatterns = [path("policy", policy, name="policy")]
