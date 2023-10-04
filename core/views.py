from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from core.models import SupportRequests
from core.serializers import SupportRequestsSerializer
from elasticsearch_dsl.connections import connections


class SupportRequestListApiView(generics.ListAPIView):
    queryset = SupportRequests.objects.all()
    serializer_class = SupportRequestsSerializer

class SupportRequestCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = SupportRequestsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SupportRequestReteriveApiView(generics.RetrieveAPIView):
#     queryset = SupportRequests.objects.all()
#     serializer_class = SupportRequestsSerializer

class SupportRequestUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = SupportRequests.objects.all()
    serializer_class = SupportRequestsSerializer
