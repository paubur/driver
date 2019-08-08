


# Create your views here.
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from forum.models import ForumPost, ForumPostAnswer
from forum.serializers import ForumPostSerializer, ForumPostAnswerSerializer
from rest_framework import generics, permissions, viewsets

from quiz.permissions import IsOwnerOrReadOnly


# class ForumPostList(generics.ListCreateAPIView):
#     queryset = ForumPost.objects.all()
#     serializer_class = ForumPostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
# class ForumPostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly]
#     queryset = ForumPost.objects.all()
#     serializer_class = ForumPostSerializer


class ForumPostViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class ForumPostAnswerList(generics.ListCreateAPIView):
#     queryset = ForumPostAnswer.objects.all()
#     serializer_class = ForumPostAnswerSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
# class ForumPostAnswerDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly]
#     queryset = ForumPost.objects.all()
#     serializer_class = ForumPostSerializer



class ForumPostAnswerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = ForumPostAnswer.objects.all()
    serializer_class = ForumPostAnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer




@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user_forum-list', request=request, format=format),
        'forumpost': reverse('forum_post-list', request=request, format=format),
        'forumpostsanswer': reverse('forum_post_answer-list', request=request, format=format),
    })