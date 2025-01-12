from rest_framework import serializers
from common.models import Group, GroupMembership
from django.contrib.auth.models import User

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
        
class GroupMembershipSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    class Meta:
        model = GroupMembership
        fields = ["id", "user", "group"]