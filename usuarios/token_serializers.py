from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import exceptions

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        return token

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        if email and password:
            user = authenticate(request=self.context.get("request"), username=email, password=password)
            if not user:
                raise exceptions.AuthenticationFailed("Credenciais inválidas", code="authentication")
        else:
            raise exceptions.AuthenticationFailed("Email e senha são obrigatórios")
        data = super().validate({"username": user.email, "password": password})
        return data
