from rest_framework import serializers
from .models import Music, Artist, Review

class MusicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist_id']

class ArtistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']

class ArtistDetailSerializers(serializers.ModelSerializer):
    music_set = MusicSerializers(many=True)
    class Meta(ArtistSerializers.Meta):
        fields = ArtistSerializers.Meta.fields + ['music_set']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['content']