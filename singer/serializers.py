from rest_framework import serializers
from .models import *

class SingerSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField(read_only=True)

    def get_songs(self, instance):
        serializer = SongSerializer(instance.songs, many=True)
        return serializer.data
    
    tag = serializers.SerializerMethodField()
    def get_tag(self, instance):
        tags = instance.tag.all()
        return [tag.name for tag in tags]
    
    class Meta:
        model = Singer
        fields = ['id', 'name', 'content', 'debut', 'songs', 'tag', 'image']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ['singer']

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'