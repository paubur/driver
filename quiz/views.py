

# Create your views here.
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from quiz.models import Advice, Quiz
from quiz.permissions import IsOwnerOrReadOnly
from quiz.serializers import AdviceSerializer, QuizSerializer
from rest_framework import generics, permissions, viewsets
from django.contrib.auth.models import User
from rest_framework.reverse import reverse



class AdviceList(generics.ListCreateAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AdviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
                          # IsOwnerOrReadOnly]


#
# class AdviceViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list`, `create`, `retrieve`,
#     `update` and `destroy` actions.
#
#     Additionally we also provide an extra `highlight` action.
#     """
#     queryset = Advice.objects.all()
#     serializer_class = AdviceSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#                           # IsOwnerOrReadOnly]



class QuizList(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def perform_create(self, serializer):
    #     user = get_object_or_404(User, user_id=self.request.data.get('user'))
    #     return serializer.save(user=user)

class QuizDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


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
        'users': reverse('user-list', request=request, format=format),
        'advices': reverse('advice-list', request=request, format=format),
        'quizes': reverse('quiz-list', request=request, format=format)
    })


# class QuizViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list`, `create`, `retrieve`,
#     `update` and `destroy` actions.
#
#     Additionally we also provide an extra `highlight` action.
#     """
#     queryset = Quiz.objects.all()
#     serializer_class = QuizSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly]
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#


