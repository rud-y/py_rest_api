from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets

class ExampleApiView(APIView):
    """Test API View"""
    serializer_class = serializers.ExampleSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete',
            'Is similar to traditional Django View',
            'Mapped manually to URLs',
        ]

        return Response({'message': 'Example:', 'an_apiview': an_apiview})

    def post(self, request):
        """Create an example message with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Welcome {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle of object update"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})
    
class ExampleViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.ExampleSerializer

    def list(self, request):
        """Return a example message"""
        a_viewset = [
            'Uses actions (list create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Example', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create a new Example message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} !'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def retrieve(self, request, pk=None):
       """Handle get object by the id"""
       return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """Handle update an object"""
        return Response({'http_methodf': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handle update the part of an objec"""
        return Response({'htttp_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        """Handle removing object"""
        return Response({'http_method', 'DELETE'})
