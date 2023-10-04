from django.db import models
from django.contrib.auth.models import User
 


# # Create your models here.
class Category(models.Model):
       name =   models.CharField(null=False,max_length=25)
       created_date = models.DateField(auto_now_add=True)
class Articles(models.Model):
    title = models.CharField(null=False,max_length=25)
    description = models.TextField(max_length=200,null=False)
    author  = models.ForeignKey(User,on_delete=models.CASCADE,related_name="author")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category")
    created_date = models.DateField(auto_now_add=True)
    
class FavoriteArticle(models.Model):
  article = models.ForeignKey(Articles,on_delete=models.CASCADE,related_name="article_fav")
  description = models.TextField(max_length=200,null=False)
  created_date = models.DateField(auto_now_add=True)
  

       
class Comment(models.Model):
       article = models.ForeignKey(Articles,on_delete=models.CASCADE,related_name="article")
       author  = models.ForeignKey(User,on_delete=models.CASCADE,related_name="authorcomment")
       description = models.TextField(null=False,max_length=25)
       created_date = models.DateField(auto_now_add=True)