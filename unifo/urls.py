from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import homepage.views
from allauth.account.views import LoginView, SignupView, LogoutView

urlpatterns = [
    path('', homepage.views.home, name='home'),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('authentication/', include('authentication.urls')),
    path('accounts/login', LoginView.as_view(), name='account_login'),
    path('accounts/signup', SignupView.as_view(), name='account_signup'),
    path('accounts/logout', LogoutView.as_view(), name='account_logout'),
    path('other/', include('other.urls')),
    path('university/', include('university.urls')),
    path('event/', include('event.urls')),
    path('compiler/', include('compile.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
