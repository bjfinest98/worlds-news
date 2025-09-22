# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('article/<slug:slug>/', views.Article_details, name= 'article_details'),
    path('category/<slug:slug>/', views.category_view, name= "category"),
    path('article/<slug:slug>/comment/', views.Post_comment, name='post_comment'),
]
