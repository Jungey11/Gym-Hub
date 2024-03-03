from django.contrib import admin
from django.urls import path
from gym.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('logout/',Logout, name="logout"),
    path('user_logout/',user_logout, name="user_logout"),
    path('user_profile/', user_profile, name="user_profile"),
    path('user_change_password/', user_change_password, name="user_change_password"),
    path('registration',registration, name="registration"),
    path('user_login/',user_login, name="user_login"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
