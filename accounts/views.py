from django.contrib.auth import get_user_model, authenticate
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed

from .serializers import SignUpSerializer

from .constants import Token


class SignUpView(APIView):

    def post(self, request):

        # initialize the serializer with data from the request body (JSON payload)
        serializer = SignUpSerializer(data=request.data)

        # Check if the data is valid (e.g., passwords match, email isn't taken, etc.)
        if serializer.is_valid(raise_exception=True):

            # save the user (calls create_user behind the scenes)
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token

            res = JsonResponse(
                {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                }
            )

            # set access token in server
            res.set_cookie(
                Token.ACCESS_TOKEN,
                access_token,
                httponly=True,
                samesite="Lax",
                max_age=15 * 60,  # 15 min
            )

            # set refresh token in server
            res.set_cookie(
                Token.REFRESH_TOKEN,
                str(object=refresh),
                httponly=True,
                samesite="Lax",
                max_age=30 * 24 * 60 * 60,  # 30 days
            )
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data.get("username"), password=request.data.get("password")
        )
        if user is None:
            return Response({"detail": "Invalid credentials"}, status=401)

        refresh_token = RefreshToken.for_user(user)
        access_token = str(refresh_token.access_token)
        res = JsonResponse(
            {
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
        )

        # important part for setting cookies in server for the authenticated
        # user for further requests:

        # set access token in server
        res.set_cookie(
            Token.ACCESS_TOKEN,
            access_token,
            httponly=True,
            samesite="Lax",
            max_age=15 * 60,  # 15 min
        )

        # set refresh token in server
        res.set_cookie(
            Token.REFRESH_TOKEN,
            str(refresh_token),
            httponly=True,
            samesite="Lax",
            max_age=30 * 24 * 60 * 60,  # 30 days
        )
        return res


class TokenRefreshView(APIView):
    def post(self, request):
        token = request.COOKIES.get(Token.REFRESH_TOKEN)
        if not token:
            raise AuthenticationFailed("Refresh token not found!")

        try:
            refresh = RefreshToken(token)
            access_token = refresh.access_token
        except:
            raise AuthenticationFailed("Invalid refresh token!")

        res = JsonResponse({"message": "Token refreshed"})
        res.set_cookie(
            Token.ACCESS_TOKEN,
            access_token,
            httponly=True,
            samesite="Lax",
            max_age=15 * 60,  # 15 min
        )
        return res


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        res = Response({"message": "Logout successful!"})
        res.delete_cookie(Token.ACCESS_TOKEN)
        res.delete_cookie(Token.REFRESH_TOKEN)
        return res


User = get_user_model()


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response(
            {
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
        )
