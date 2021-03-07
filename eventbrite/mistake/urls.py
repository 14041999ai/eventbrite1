from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload,  name='upload'),
    path('', views.display,  name='display'),
]