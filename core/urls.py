from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path("support_request/list/", SupportRequestListApiView.as_view(), name='support_request_list'),
    path("support_request/", SupportRequestCreateApiView.as_view(), name='support_request_create'),
    # path("support_request/<int:pk>/", SupportRequestReteriveApiView.as_view(), name='support_request_view'),
    path("support_request/<int:pk>/update/", SupportRequestUpdateApiView.as_view(), name='support_request_update'),
]
