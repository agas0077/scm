# Third Party Library
from core.views import policy
from django.urls import path

app_name = "core"

urlpatterns = [path("policy", policy, name="policy")]
