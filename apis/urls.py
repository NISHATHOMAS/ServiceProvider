from django.urls import path

from .views import ServiceAreasListCreateApiView, ProvidersListCreateApiView, GetPolygonApiView

urlpatterns = [
    path("providers", ProvidersListCreateApiView.as_view(), name="Providers"),
    path("service-areas", ServiceAreasListCreateApiView.as_view(), name="ServiceAreas"),
    path("get-polygon", GetPolygonApiView.as_view(), name="GetPolygon"),
 ]
