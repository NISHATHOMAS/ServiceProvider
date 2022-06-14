from django.urls import path

from .views import ServiceAreasListCreateApiView

urlpatterns = [path("", ServiceAreasListCreateApiView.as_view(), name="ServiceAreas"),

               ]
