from django.shortcuts import render
from rest_framework.response import Response
from .models import*
from rest_framework import viewsets,status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import*
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

class RegisterViewSet(viewsets.ViewSet):
    def create(self,request):
        name=request.data.get('name')
        email=request.data.get('email')
        password=request.data.get('password')
        confirm_password=request.data.get('confirm_password')
        
        if password!=confirm_password:
            return Response({"error":"password does not match"})
        
        user_data={
            "name":name,
            "email":email,
            "password":make_password(password),
            "confirm_password":make_password(confirm_password)
            
        }        
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class Login(viewsets.ViewSet):
    permission_classes = [AllowAny]
    def create(self,request):
        email= request.data.get('email')
        password=request.data.get('password')
        
        try:
            user = User.objects.get(email=email) 
        except user.DoesNotExist:
            return Response({"error":'User not found'},status=status.HTTP_404_NOT_FOUND)
        
        if not check_password(password,user.password):
            return Response({"error":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        return Response({
            "message":"Logged in sucessfully..",
            'refresh':str(refresh),
            'access':str(refresh.access_token),
        },status=status.HTTP_200_OK)
        
        
class TaskView(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]
    def create(self,request):
        print("Authenticated User:", request.user)  
        print("Authenticated User ID:", request.user.id) 
    
        
        title = request.data.get('title')
        description = request.data.get('description')
        completed = request.data.get('completed',False)
        
        task_data = {
            
            "title":title,
            "description":description,
            "completed":completed,
            "user":request.user.id
        }
        print(task_data)
        serializer = TaskSerializer(data=task_data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                "task_data":serializer.data
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
    def list(self,request):
        task_all = Task.objects.all()
        serializer = TaskSerializer(task_all,many=True)
        return Response(serializer.data)       
        


        
        
        
class ResetPasswordView(viewsets.ViewSet):
    # authentication_classes = [JWTAuthentication] 
    permission_classes = [AllowAny]
    def create(self, request):
        email = request.data.get("email")
        new_password = request.data.get("new_password")

        try:
            user = User.objects.get(email=email)
            user.password = make_password(new_password)  # Hash new password
            user.save()
            return Response({"message": "Password reset successfully!"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)      