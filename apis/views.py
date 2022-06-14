from django.db.models import Q
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apis.models import ServiceAreas, Provider, GeoJson
from apis.serializers import ServiceAreaSerializer, ProviderSerializer


class ProvidersListCreateApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        List all service areas
        """
        providers = Provider.objects.filter(user=request.user)
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create the providers   with the given data
        """

        serializer = ProviderSerializer(data=kwargs)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceAreasListCreateApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        List all service areas
        """
        service_area = ServiceAreas.objects.filter(provider__user=request.user)
        serializer = ServiceAreaSerializer(service_area, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create the Service Area with the given data
        """

        serializer = ServiceAreaSerializer(data=kwargs)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetPolygonApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        List all service areas for the given lat lon pair
        """
        lat = request.GET.get("lat")
        lon = request.GET.get("lon")
        geoJson = GeoJson.objects.filter(Q(latitude=lat) | Q(longitude=lon))
        serializer = ServiceAreaSerializer(geoJson, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
