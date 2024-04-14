from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers
# Create your views here.

class HelloAPiView(APIView):
    """ApI view test class"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URls',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request, format=None):
        """Resturn a message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        """Handle updating an object (Updating all)"""
        return Response({'method': 'PUT'})


    def patch(self, request, pk=None):
        """Handlle patching an object (Partial Update)"""
        return Response({'method': 'PATCH'})
    

    def delete(self, request, pk=None):
        """Handlle deleting an object"""
        return Response({'method': 'DELETE'})
    

class HelloViewSet(viewsets.ViewSet):
    """ Test API viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (List, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more funcitonality with less code',
        ]
    
        return Response({'message': 'Hello', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create a new hello message"""

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


    def retrieve(self, request, pk=None):
        """To Retreive an object using obj pk"""
        return Response({'http_method': 'GET'})
    

    def update(self, request, pk=None):
        """To Update an object based obj pk (put / full update)"""
        return Response({'http_method': 'PUT'})
    

    def partial_update(self, request, pk=None):
        """To partially Update an object based obj pk (Patch update)"""
        return Response({'http_method': 'PATCH'})
    

    def destroy(self, request, pk=None):
        """To Delete an object based obj pk (Patch update)"""
        return Response({'http_method': 'DELETE'})
    
