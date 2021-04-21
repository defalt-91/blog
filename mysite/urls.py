from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
import Accounts.views as Accounts_views
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView
from survey.views import SurveyViewset, ChoiceViewset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='Accounts/login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Accounts/logout.html'),
         name='logout'),
    path('register/', Accounts_views.register, name='register'),
    path('profile/', Accounts_views.profile, name="profile"),
    path('password_reset/done/', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('api/v2/',include('survey.urls'))



]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT)
