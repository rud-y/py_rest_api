from rest_framework.views import APIView
from rest_framework.response import Response

class ExampleApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete',
            'Is similar to traditional Django View',
            'Mapped manually to URLs',
        ]

        return Response({'message': 'Example', 'an_apiview': an_apiview})