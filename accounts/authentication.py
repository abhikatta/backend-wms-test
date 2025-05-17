from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .constants import Token


class CookieJWTAuthentication(JWTAuthentication):
    # by default simple jwt/drf dont know, uses Authorization header for getting the tokens,
    # using this to change that to grab tokens from the cookies that are sent from frontend
    def authenticate(self, request):
        access_token = request.COOKIES.get(Token.ACCESS_TOKEN)
        if not access_token:
            return None

        try:
            validated_token = self.get_validated_token(access_token)
            return self.get_user(validated_token), validated_token
        except Exception:
            raise AuthenticationFailed("Invalid token.")
