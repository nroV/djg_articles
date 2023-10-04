from django.shortcuts import render
from rest_framework.decorators import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import *
from .serializers import *
from django.shortcuts import *
from rest_framework.status import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token



from drf_yasg.utils import swagger_auto_schema
# from rest_framework.decorators import api_view,
from rest_framework import viewsets

# Create your views here.
# @swagger_auto_schema(method='POST', request_body=ArticleSerializerV2)
# @swagger_auto_schema(method='PATCH', request_body=ArticleSerializerV2)
# @swagger_auto_schema(method='GET')
# @swagger_auto_schema(method='DELETE')

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = FavSerializerGet
    queryset = FavoriteArticle.objects.all()

@swagger_auto_schema(method='POST', request_body=FavSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def articlefavorite(request,pk):
    if request.method == "POST":
        serializers = FavSerializer(data=request.data)
        if serializers.is_valid():
            article = Articles.objects.filter(pk =pk).first()
            if article is not None:
             serializers.save(article = article)
             return Response(serializers.data,HTTP_200_OK)
        else:
            return Response(serializers.errors,HTTP_400_BAD_REQUEST)
       
    pass

class Categories(generics.ListCreateAPIView):
    
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
    
class CommentController(generics.ListAPIView):
    
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
class CommentRUD(generics.RetrieveAPIView):
      
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
class CategoriesRUD(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
    

# @swagger_auto_schema(method='GET',operation_id="Articles",operation_summary="Article",tags="Articles")
@swagger_auto_schema(method='POST', request_body=CommentSerializer)
@api_view(['POST','PUT','DELETE'])
def CommentArticle(request,*args, **kwargs):
    if request.method == "POST":
     serializers = CommentSerializer(data=request.data)
     if serializers.is_valid():
         article = Articles.objects.get(pk = kwargs.get('pk',None))
         serializers.save(author = request.user,article = article)
         return Response(serializers.data,status=HTTP_200_OK)
     else:
         return Response(serializers.errors,status=HTTP_400_BAD_REQUEST)
            
    
    pass

@swagger_auto_schema(method='POST', request_body=ArticleSerializerV2)
@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def articles(request):
    if request.method == "GET":
     article = Articles.objects.all()
     serializers = ArticleSerializer(Articles.objects.all(),many=True)

     return Response(serializers.data)
    if request.method == "POST":
     serializers = ArticleSerializerV2(data=request.data)
     if serializers.is_valid():
        print(request.user)

        user = User.objects.get(username=request.user.username)
        serializers.save(author =user,
                         category = serializers.validated_data['category'])
        return Response(serializers.data)
     else :
        return Response(serializers.errors)
    pass


@api_view(['GET','PUT','DELETE'])
def article(request,*args, **kwargs):
    print(kwargs.get('pk'))
    pk = kwargs.get('pk')
    article = get_object_or_404(Articles,pk=pk)
    serializers = ArticleSerializer(article)
    return Response(serializers.data) 
    pass


@swagger_auto_schema(method="POST", request_body=UserSerializer)
@api_view(['POST'])

def login(request):
    
    if request.method == "POST":
     serializers = UserSerializer(data=request.data)     
     if serializers.is_valid():
     
         user = User.objects.filter(email = serializers.validated_data['email']).first()
         if user is None:
             return Response( {
                 "message":"user does not exist"
             })
         else:
            if user.check_password(serializers.validated_data['password']) :
             token, created = Token.objects.get_or_create(user=user)
             data = {
                "token":token.key,
                "data":serializers.validated_data['email']
             }
             return Response(  data,status=HTTP_201_CREATED)
            else:
                
             
           
            
             return Response( {
                  "message":"wrong password"
             })

         
         pass
     else:
         return Response(serializers.errors)
         pass   
        


@swagger_auto_schema(method="POST", request_body=UserSerializer)
@api_view(['POST'])

def signup(request):
   if request.method == "POST":
     serializers = UserSerializer(data=request.data)     
     if serializers.is_valid():
     
         user = User.objects.filter(email = serializers.validated_data['email']).first()
         if user is not None:
             return Response( {
                 "message":"user has registered"
             })
         else:
             
             instance= serializers.save()
             registereduser =User.objects.get(email = serializers.validated_data['email'])
             registereduser.set_password( serializers.validated_data['password'])
             registereduser.save()


             
           
             token= Token.objects.create(user=  instance)
             data = {
                "token": token.key,
                "data":serializers.data
             }
             return Response( data,status=HTTP_201_CREATED)


         

     else:
         return Response(serializers.errors)
         pass   
           
    

@api_view(['POST'])

def logout(request):
    
    if request.method == "POST":
        
         request.user.auth_token.delete()
        #  print( request.user.auth_token.delete())
         return Response({
             'message':'user has been logout'
         })

            
        
    pass