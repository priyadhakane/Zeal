from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import profile_view, profile_update, change_password

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('', views.dashboard, name='dashboard'),
    path('manage-course', views.courses, name='courses'),

    path('profile/', profile_view, name='profile'),
    path('profile/update/', profile_update, name='profile_update'),
    path('profile/change-password/', change_password, name='change_password')
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)