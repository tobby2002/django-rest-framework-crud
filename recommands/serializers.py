from rest_framework import serializers
from .models import Recommand


class RecommandSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = Recommand
        fields = ('label', 'qid', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'docid', 'q', 'title', 'content')
