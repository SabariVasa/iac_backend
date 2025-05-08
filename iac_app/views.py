# views.py
from rest_framework.views import APIView
from rest_framework import status
# from utils.response import success_response, error_response
from .utils.response import success_response, error_response
from .serializers import RegisterSerializer, LoginSerializer
from .models import User

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return success_response(
                data={"user_id": str(user.id), "email": user.email},
                message="User registered successfully.",
                status_code=status.HTTP_201_CREATED
            )
        return error_response(message="Invalid data", errors=serializer.errors)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects(email=request.data['email']).first()
            return success_response(
                data={"user_id": str(user.id)},
                message="Login successful"
            )
        return error_response(message="Invalid credentials", errors=serializer.errors)
