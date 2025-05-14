from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpSerializer(serializers.ModelSerializer):
    # write_only := do not send in response ig
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password", "confirm_password")

    #  --------------------
    # this validate() function is basically a hidden input that runs when this is_valid function is called on this serializer

    # serializer.is_valid() does 3 things under the hood (another shitty hidden input and hidden output arch):

    # according to the LLM, this serializer.is_valid():
    # Runs field validation (e.g., checks CharField, EmailField, required fields, etc.).
    # Calls your validate() method if defined — that's where we check if the passwords match.
    # Saves any validation errors into serializer.errors.
    # ---------------------
    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match!"}
            )
        if User.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError(
                {"email": "User with this email already exists!"}
            )
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        # ---------------------
        # confirm password not needed so popping it off, why? - not sure

        # as per LLM:
        # ensures that you remove it before passing the rest of the validated data to create_user(), which only expects fields like username, email, password, etc.
        # If you don’t pop it and try passing all of validated_data, you’ll get an error
        # ---------------------

        user = User.objects.create_user(
            username=validated_data[
                "email"
            ],  # as email has to unique and username is used for ex., in forgot password where user puts in email
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        return user

    # when this serializer is used in a response, this function will attach/update data in response
    # which is basically when the user signs up
    def to_representation(self, instance):
        # generate refresh and access tokens for the newly created user
        tokens = RefreshToken.for_user(instance)

        return {
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "email": instance.email,
            "refresh": str(tokens),  # used to get new access tokens - long lived
            "access": str(tokens.access_token),  # short lived token
        }
