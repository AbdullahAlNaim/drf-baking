from rest_framework import serializers
from .models import Cakes

class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cakes
        fields = '__all__' 