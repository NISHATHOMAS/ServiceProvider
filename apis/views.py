from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apis.models import ServiceAreas
from apis.serializers import ServiceAreaSerializer


class ServiceAreasListCreateApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        List all service areas
        """
        service_area = ServiceAreas.objects.filter(user=request.user.id)
        serializer = ServiceAreaSerializer(service_area, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create the Service Area with the given data
        """
        data = {
            'task': request.data.get('task'),
            'user': request.user.id
        }
        serializer = ServiceAreaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


