from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignUpSerializer


class SignUpView(APIView):

    def post(self, request):

        # initialize the serializer with data from the request body (JSON payload)
        serializer = SignUpSerializer(data=request.data)

        # Check if the data is valid (e.g., passwords match, email isn't taken, etc.)
        if serializer.is_valid(raise_exception=True):

            # save the user (calls create_user behind the scenes)
            user = serializer.save()
            return Response(
                serializer.to_representation(user), status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
