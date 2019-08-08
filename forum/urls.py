from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from forum import views
from forum.views import ForumPostViewSet, ForumPostAnswerViewSet, api_root

# urlpatterns = [
#     # path('adm/', admin.site.urls),
#     path('forum/', views.ForumPostList.as_view(), name='forum_post-list'),
#     path('forum/<int:pk>/', views.ForumPostDetail.as_view(), name='forum_post-detail'),
#     path('forum_answer/', views.ForumPostAnswerList.as_view(), name='forum_post_answer-list'),
#     path('forum_answer/<int:pk>/', views.ForumPostAnswerDetail.as_view(), name='forum_post_answer-detail'),
#     path('users_forum/', views.UserList.as_view(), name='user_forum-list'),
#     path('users_forum/<int:pk>/', views.UserDetail.as_view(), name='user_forum-detail'),
# ]

# forumpost_list = ForumPostViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# forumpost_detail = ForumPostViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# forumpost_answer_list = ForumPostAnswerViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# forumpost_answer_detail = ForumPostAnswerViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# user_forum_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_forum_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# # urlpatterns = format_suffix_patterns(urlpatterns)
#
# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('forum/', forumpost_list, name='forum_post-list'),
#     path('forum/<int:pk>/', forumpost_detail, name='forum_post-detail'),
#     path('forum_answer/', forumpost_answer_list, name='forum_post_answer-list'),
#     path('forum_answer/<int:pk>/', forumpost_answer_detail, name='forum_post_answer-detail'),
#     path('users_forum/', user_forum_list, name='user_forum-list'),
#     path('users_forum/<int:pk>/', user_forum_detail, name='user_forum-detail')
# ])


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'forum', views.ForumPostViewSet)
router.register(r'forum-posts', views.ForumPostAnswerViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]