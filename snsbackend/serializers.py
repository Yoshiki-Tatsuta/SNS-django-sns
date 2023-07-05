from django.contrib.auth.models import User
from rest_framework import serializers
from .models import SnsPost, UserProfile

class SnsPostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # ユーザーの選択フィールドを追加

    class Meta:
        model = SnsPost
        fields = ['id', 'content', 'image', 'user', 'username', 'created_at']
        
    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     validated_data['user'] = user
    #     return super().create(validated_data)
        
