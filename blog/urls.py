from django.urls import path, include
from . import views
import rest_auth
from rest_framework.routers import SimpleRouter
from .views import (PostlistvieW,
                    DetailvieW, CreatevieW,
                    UpdatevieW, DeletevieW,
                    UserpostlistvieW,
                    VueViews,
                    PostViewset,VueView)
from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='Blog API')

urlpatterns = [
    path('', PostlistvieW.as_view(), name='blog-home'),
    path('vueapi/',views.VueView,name='Vuex'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', DetailvieW.as_view(), name='post-detail'),
    path('post/new/', CreatevieW.as_view(), name='post-new'),
    path('post/<int:pk>/update/', UpdatevieW.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DeletevieW.as_view(), name='post-delete'),
    path('post/<str:username>', UserpostlistvieW.as_view(), name="user-posts"),
    path('about/', views.about, name='blog-about'),
    path('vue/', VueViews, name='Vue'),
    path('api/', include('rest_framework.urls')),  # login for browsable api
    path('api/auth/', include('rest_auth.urls')),  # login for tokenbaseapi
    path('api/auth/',  # new
         include('rest_auth.registration.urls')),
    path('api/schemas/', schema_view)

    # path('api/v1/', PostViewset),
]

router = SimpleRouter()
router.register('api/v1', PostViewset, basename='post-api')
urlpatterns += router.urls
