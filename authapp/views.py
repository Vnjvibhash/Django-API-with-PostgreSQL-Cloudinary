from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import User
from django.core.mail import send_mail
from django.contrib.auth import login, logout
import random

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            otp = str(random.randint(100000, 999999))
            user.otp = otp
            user.save()
            print(f"[DEV] OTP for {user.email} is: {otp}")
            send_mail(
                subject="Verify your email",
                message=f"Your OTP is: {otp}",
                from_email="no-reply@example.com",
                recipient_list=[user.email],
                fail_silently=True,
            )

            return Response({
                'message': 'User registered successfully. OTP sent to email.',
                'user': {
                    'email': user.email,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'profile_photo': str(user.profile_photo),
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResendOTPView(APIView):
    def post(self, request):
        serializer = ResendOTPSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
                otp = str(random.randint(100000, 999999))
                user.otp = otp
                user.save()
                print(f"[DEV] OTP for {email} is: {otp}")

                return Response({"message": "OTP resent. Check console."}, status=200)
            except User.DoesNotExist:
                return Response({"error": "User not found."}, status=404)
        return Response(serializer.errors, status=400)

class VerifyOTPView(APIView):
    def post(self, request):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(email=serializer.validated_data['email'])
                if user.otp == serializer.validated_data['otp']:
                    user.is_verified = True
                    user.otp = None
                    user.save()
                    return Response({'message': 'Account verified'})
                else:
                    return Response({'error': 'Invalid OTP'}, status=400)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=404)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            if user.is_verified:
                login(request, user)
                user_data = UserSerializer(user).data  # Serialize user data
                return Response({
                    'message': 'Login successful',
                    'user': user_data
                }, status=200)
            else:
                return Response({'error': 'Email not verified'}, status=403)
        return Response(serializer.errors, status=400)


class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(email=serializer.validated_data['email'])
                otp = str(random.randint(100000, 999999))
                user.otp = otp
                user.save()
                send_mail(
                    subject="Password Reset OTP",
                    message=f"Your OTP is {otp}",
                    from_email="noreply@example.com",
                    recipient_list=[user.email],
                )
                return Response({'message': 'OTP sent to email'})
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=404)
        return Response(serializer.errors, status=400)
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful"}, status=205)
        except Exception as e:
            return Response({"error": "Invalid token or already blacklisted"}, status=400)
