from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from custom_user.Serializers import CustomUserSerializer

User=get_user_model()

#generating access and refresh token

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
def user_register(request):
    email = request.data.get('email')
    password = request.data.get('password')
    name = request.data.get('name')

    if email is None or password is None or name is None:
        return Response({'success':False,'message': 'Please provide valid details'}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(email=email).exists():
        return Response({'success':False,'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user=User.objects.create_user(email=email, password=password,name=name)
    except Exception as e:
        return Response({'success':False,'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    tokens=get_tokens_for_user(user)
    data={
        'success':True,
        'message':'User created successfully',
        'tokens': tokens,
        'user': CustomUserSerializer(user).data,
    }
    return Response(data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def user_login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if email is None or password is None:
        return Response({'success':False,'message': 'Please provide valid details'}, status=status.HTTP_400_BAD_REQUEST)
    if not User.objects.filter(email=email).exists():
        return Response({'success':False,'message': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.get(email=email)
    if not user.check_password(password):
        return Response({'success':False,'message': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    tokens=get_tokens_for_user(user)
    data={
        'success':True,
        'message':'User login successfully',
        'tokens': tokens,
        'user': CustomUserSerializer(user).data,
    }
    return Response(data, status=status.HTTP_200_OK)

