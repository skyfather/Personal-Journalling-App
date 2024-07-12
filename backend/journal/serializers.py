from .models import Category, Journal
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Journal
        fields= '__all__'
        # read_only_fields = ['owner']