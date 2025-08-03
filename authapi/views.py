from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser

User = get_user_model()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    return Response({
        'id': user.id,
        'email': user.email,
        'name': user.name,
        'profilePicture': request.build_absolute_uri(user.profilePicture.url) if user.profilePicture else None,
    })


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, username=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user_id': user.id,
                'email': user.email,
                'name': user.name,
                'profilePicture': request.build_absolute_uri(user.profilePicture.url) if user.profilePicture else None,
            })
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]  # For form-data or file uploads

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        name = request.data.get('name')
        profilePicture = request.FILES.get('profilePicture')  # Optional

        # Validate required fields
        if not email or not password or not name:
            return Response({"error": "Name, email, and password are required"}, status=400)

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already exists"}, status=400)

        # Create user
        user = User.objects.create_user(
            email=email,
            password=password,
            name=name,
        )

        # If profilePicture is provided (web form or upload), save it
        if profilePicture:
            user.profilePicture = profilePicture
            user.save()

        return Response({"message": "User registered successfully"}, status=201)


@csrf_exempt
def signup_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            name = data.get('name')
            # You can extend this to accept a base64-encoded image if needed.

            if not email or not password or not name:
                return JsonResponse({'error': 'Name, email, and password are required'}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'error': 'User already exists'}, status=400)

            user = User.objects.create_user(email=email, password=password, name=name)
            return JsonResponse({'message': 'Account created successfully!'}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)



class EditProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request):
        user = request.user
        name = request.data.get('name', user.name)
        email = request.data.get('email', user.email)
        phone_number = request.data.get('phone_number', user.phone_number)
        birth_date = request.data.get('birth_date', user.birth_date)
        profilePicture = request.FILES.get('profilePicture')

        # Assign updated values
        user.name = name
        user.email = email
        user.phone_number = phone_number
        user.birth_date = birth_date

        if profilePicture:
            user.profilePicture = profilePicture

        user.save()

        return Response({
            'message': 'Profile updated successfully',
            'name': user.name,
            'email': user.email,
            'phone_number': user.phone_number,
            'birth_date': user.birth_date,
            'profilePicture': request.build_absolute_uri(user.profilePicture.url) if user.profilePicture else None
        })
