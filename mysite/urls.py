from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
import Accounts.views as Accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='Accounts/login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Accounts/logout.html'),
         name='logout'),
    path('register/', Accounts_views.register, name='register'),
    path('profile/', Accounts_views.profile, name="profile"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
