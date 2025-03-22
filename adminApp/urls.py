from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('', views.dashboard, name='dashboard'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)