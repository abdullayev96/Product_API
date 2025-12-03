from rest_framework import serializers
from .models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
       model = Category
       fields = ('id', "name", "image", "slug")



