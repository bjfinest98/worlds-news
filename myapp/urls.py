# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('/myproject', views.home, name='home'),
    path('article/<slug:slug>/', views.article_detail, name= 'article_detail'),
    path('article/<slug:slug>/', views.category, name= "category"),
    path('article/<slug:slug>/', views.post_comment, name='post_comment'),
]
