from rest_framework import serializers
from .models import EmailTemplate


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = ['id', 'name', 'subject', 'body']
