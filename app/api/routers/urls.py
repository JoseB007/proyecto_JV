from django.urls import path

from app.api.views.views import ApellidoView, CompartirView


urlpatterns = [
    path("apellido/", ApellidoView.as_view(), name="apellido"),
    path("compartir/", CompartirView.as_view(), name="compartir"),
]