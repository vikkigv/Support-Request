from rest_framework import serializers

from core.models import SupportRequests


class SupportRequestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SupportRequests
        fields = "__all__"