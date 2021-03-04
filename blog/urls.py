from django.urls import path
from . import views
from .views import (PostlistvieW,
                    DetailvieW, CreatevieW,
                    UpdatevieW, DeletevieW,
                    UserpostlistvieW,
                    VueViews)

urlpatterns = [
    path('', PostlistvieW.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', DetailvieW.as_view(), name='post-detail'),
    path('post/new/', CreatevieW.as_view(), name='post-new'),
    path('post/<int:pk>/update/', UpdatevieW.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DeletevieW.as_view(), name='post-delete'),
    path('post/<str:username>', UserpostlistvieW.as_view(), name="user-posts"),
    path('about/', views.about, name='blog-about'),
    path('vue/',VueViews, name='Vue'),
]
