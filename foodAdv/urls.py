"""
URL configuration for foodAdv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from fSite.views import index, agreement, log_in, register, profile_view, poll, log_out, profile_edit, changerest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index  , name='home'),
    path('agreement/', agreement),
    path('login/', log_in, name='login'),
    path('registration/', register, name='register'),
    path('logout/', log_out, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('edit/', profile_edit, name='profile_edit'),
    path('changerest/', changerest, name='changerest'),
    path('poll/', poll)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
