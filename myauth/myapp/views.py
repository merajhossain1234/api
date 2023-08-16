from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import LoginSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import StudentSerializer
from .models import Student
# Create your views here.



class SignupAPIView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={'status':status.HTTP_201_CREATED}
            return Response(res,status=status.HTTP_201_CREATED)
        res={'status':status.HTTP_400_BAD_REQUEST,'data':serializer.errors}
        return Response(res, status = status.HTTP_400_BAD_REQUEST) 
    
    
    
    
    
    
class LoginAPIView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
  
    def post(self,request):
            serializer = LoginSerializer(data = request.data)
            if serializer.is_valid():
                    username = serializer.validated_data["username"]
                    password = serializer.validated_data["password"]
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        """We are reterving the token for authenticated user."""
                        token = Token.objects.get(user=user)
                        response = {
                               "status": status.HTTP_200_OK,
                               "message": "success",
                               "data": {
                                       "Token" : token.key
                                       }
                               }
                        return Response(response, status = status.HTTP_200_OK)
                    else :
                        response = {
                               "status": status.HTTP_401_UNAUTHORIZED,
                               "message": "Invalid Email or Password",
                               }
                        return Response(response, status = status.HTTP_401_UNAUTHORIZED)
            response = {
                 "status": status.HTTP_400_BAD_REQUEST,
                 "message": "bad request",
                 "data": serializer.errors
                 }
            return Response(response, status = status.HTTP_400_BAD_REQUEST)

class StudentAPIViewforpost(APIView): 
    authentication_classes=[TokenAuthentication]
    permission_classes =[IsAuthenticated]   
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": status.HTTP_201_CREATED,
                "message": "Student created successfully",
                "data": serializer.data,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Invalid data",
                "errors": serializer.errors,
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)        
        






class StudentAPIView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes =[IsAuthenticated] 
    
    def get(self, request):
        data=Student.objects.all()
        serializer=StudentSerializer(data,many=True)
        response={
            "status":status.HTTP_200_OK,
            "message":"success",
            "data":serializer.data,
        } 
        
        return Response(response,status=status.HTTP_200_OK) 
     
   
        
        
        
        
        
class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


