from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from common.models import Group, GroupMembership
from api.serializers.Group_serializer import GroupSerializer, GroupMembershipSerializer
from django.contrib.auth.models import User


class GroupListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        queryset = Group.objects.all()
        serializer = GroupSerializer(queryset, many=True)
        return Response(data=serializer.data)
    
    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors)
    
    
class JoinGroupView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        group_id = request.data.get("id")
        group = Group.objects.filter(id=group_id).first()
        if group is None:
            raise NotFound("group not found")
        user_group = GroupMembership.objects.create(user=request.user, group=group)
        serializer = GroupMembershipSerializer(user_group)
        return Response(serializer.data)
    