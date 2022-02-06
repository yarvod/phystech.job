from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    model = Post
    fields = ('id', 'title', 'body', 'created')
