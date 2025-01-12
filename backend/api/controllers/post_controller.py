from rest_framework.views import APIView
from rest_framework.response import Response
from common.models import Post
from api.serializers.post_serializer import PostSerializer


class PostView(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
