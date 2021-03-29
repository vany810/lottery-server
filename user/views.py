from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from .serialziers import RegisterSerializer, UserSerializer
from .models import User


class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    @extend_schema(
        request=RegisterSerializer,
        responses={201: UserSerializer},
        description='用户注册',
        summary='用户注册',
        tags=['用户接口']
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(self.request)
        headers = self.get_success_headers(serializer.data)
        response_data = UserSerializer(user).data
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
