"""
URL configuration for KurzFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from KurzFinalApp import views as Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Views.home, name='home'),
    # path('index/', Views.index),
    # path(r'^galerie$', 'galerie', name='galerie'),
    path('galerie/', Views.galerie, name='galerie'),
    path('kontakty/', Views.kontakty, name='kontakty'),
    # path('psiHra/', Views.psiHra, name='psiHra'),
    path('dog/<int:dog_id>', Views.detail, name='detail'),
    path('signup/', Views.signup, name='signup'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)