import serializers as serializers
from rest_framework import serializers
from . import models

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ( 'id','title','content','create','update',)
        model = models.Post
