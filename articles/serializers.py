from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
  class Meta:
   model = User
   fields = ['email','password']
class CategorySerializer(serializers.ModelSerializer):

    
 class Meta:
  model =Category   
  fields ='__all__'
class ArticleSerializerV2(serializers.ModelSerializer):

#  author = UserSerializer(read_only=True)
 class Meta:
  model = Articles
  fields = ['title','description','category']
class ArticleSerializer(serializers.ModelSerializer):

 author = UserSerializer(read_only=True)
 category = CategorySerializer(read_only=True)
 class Meta:
  model = Articles
  fields = '__all__'

class FavSerializer(serializers.ModelSerializer):

  class Meta:
   model =FavoriteArticle
   fields = ('description',)
class FavSerializerGet(serializers.ModelSerializer):
  article = ArticleSerializerV2(read_only=True)
  class Meta:
   model =FavoriteArticle
   fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
  
  author = UserSerializer(read_only=True)
  article = ArticleSerializer(read_only = True)
    
  class Meta:
   model = Comment
   fields ='__all__'


