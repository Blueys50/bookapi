from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'created_date', 'tag', 'image']
        read_only_fields = ['created_date']
