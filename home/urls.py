from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView,   name='home'),
    path('login/', LoginView,   name='login'),
    path('logout/', LogoutView,   name='logout'),
    path('register/', RegisterView,   name='register'),
    path('profile/<int:pk>/', ProfileView,   name='profile'),
    path('create-post/<int:pk>/', CreatePostView,   name='create_post'),
    path('posts/<int:pk>/', PostsView,   name='posts'),
    path('edit-post/<int:pk>/', EditPostView,   name='edit-post'),
    path('comment/<int:pk>/', CommentsView,   name='comment'),
    path('edit-comment/', EditCommentView,   name='edit_comments'),
    path('delete-comment/', DeleteCommentView,   name='delete_comments'),
]