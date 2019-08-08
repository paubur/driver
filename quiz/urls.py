from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from quiz import views
# from quiz.views import AdviceViewSet, QuizViewSet, UserViewSet, api_root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('advices/', views.AdviceList.as_view(), name='advice-list'),
    path('advices/<int:pk>/', views.AdviceDetail.as_view(), name='advice-detail'),
    path('quizes/', views.QuizList.as_view(), name='quiz-list'),
    path('quizes/<int:pk>/', views.QuizDetail.as_view(), name='quiz-detail'),
    # path('users/', views.UserList.as_view(), name='user-list'),
    # path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]

# advice_list = AdviceViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# advice_detail = AdviceViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# quiz_list = QuizViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# quiz_detail = QuizViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
#
# # urlpatterns = format_suffix_patterns(urlpatterns)
#
#
# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('advices/', advice_list, name='advice-list'),
#     path('advice/<int:pk>/', advice_detail, name='advice-detail'),
#     path('quizes/', quiz_list, name='quiz-list'),
#     path('quiz/<int:pk>/', quiz_detail, name='quiz-detail'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])



# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# # router.register(r'advices', views.AdviceViewSet)
# router.register(r'quizes', views.QuizViewSet)
# router.register(r'users', views.UserViewSet)
#
# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]