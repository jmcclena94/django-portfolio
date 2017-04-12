from rest_framework import serializers
from subscribe.models import Emails


class EmailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emails
        fields = (
            'email',
            )
