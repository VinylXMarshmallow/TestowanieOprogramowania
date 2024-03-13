"""
URL configuration for testproject project.

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def trigger_error(request):
    division_by_zero = 1 / 0
def index_error(request):
    my_list = [1, 2, 3]
    value = my_list[4]  # Ten kod spowoduje IndexError

def index(request):
        return HttpResponse("Welcome to my Django project!")

urlpatterns = [
    path('', index),  # Handle the root URL
    path('index-error/', index_error)
    path('sentry-debug/', trigger_error, ),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




