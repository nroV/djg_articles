"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('favorite', views.ArticleViewSet, basename='favorite')
# urlpatterns = router.urls

urlpatterns = [
    #this is article routes
    path('article/',views.articles,name="article"),
    path('article/<int:pk>/',views.article,name="article"),
    
        path('',include(router.urls)),
        path('favorite/article/<int:pk>',views.articlefavorite),
   #this is category routes
   
   path('category/',views.Categories.as_view(),name="category"),
      path('category/<int:pk>/',views.CategoriesRUD.as_view(),name="category-v2"),
         path('category/article',views.CategoriesRUD.as_view(),name="category-v2"),
      
      
         #this is comment routes
   
     path('comment/',views.CommentController.as_view(),name="comment"),
      path('comment/article/<int:pk>',views.CommentArticle,name="comment-2"),
      path('comment/<int:pk>/',views.CommentRUD.as_view(),name="comment"),
      
      
      path('user/login',views.login),
         path('user/signup',views.signup),
            path('user/logout',views.logout),
      
      
      
      
]
