# Views in Django are responsible for handling the endpoint logic, they take the request, perform some operations eg. load model from database, serialize it into JSON format and return the HTTP Response.

from rest_framework import viewsets
from .models import item
from .serializers import ItemSerializer


# - handle the GET and POST operations for the Item model.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = item.objects.all()
    serializer_class = ItemSerializer


""" 
in this method we have define each method (e.g. get, post) manually but More control and customization
You define URLs explicitly via urls.py and path() or re_path()

from rest_framework.views import APIView
from rest_framework.response import Response

class ItemsView(APIView):
    def get(self, request):
        items = item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
"""
from django.shortcuts import render


def index_view(request):
    return render(request, "index.html")
