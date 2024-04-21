from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserSerializer

class SignUpView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status

class SignInView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        # Token işlemi yapılır
        token, created = Token.objects.get_or_create(user=user)
        
        # Başarılı giriş mesajı ve token yanıt olarak döndürülür
        return Response({'message': 'Sign in successful', 'token': token.key}, status=status.HTTP_200_OK)
