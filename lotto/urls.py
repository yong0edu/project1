from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='lotto'),
 path('form', views.post),
 path('detail', views.detail, name='detail'),
 path('detail/<int:num>', views.detail2, name='detail2'),
 path('join', views.join, name='join'),
 path('id_check', views.id_check, name='id_check'),
 path('login', views.login, name='login'),
]
