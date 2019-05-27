from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
	path('',TemplateView.as_view(template_name='home.html')),
	path('login',LoginView.as_view(template_name='login.html')),
	path('api/article/',include('article.api.urls',namespace='posts-api')),
    path('admin/', admin.site.urls),
]
