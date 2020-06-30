# from rest_framework.response import  Response
# from rest_framework.views import APIView
# from rest_framework import serializers
# from django.contrib.auth.models import UserAPI
# from .models import UserAPI
# # Create your views here.
#
# class UserAPISerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = UserAPI
#         fields = ('name', 'email', 'password')
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from .models import UsersAPI
from rest_framework import serializers
from .serializers import UsersAPI

class UserApiSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        return UsersAPI.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.name)
        instance.password = validated_data.get('password', instance.password)

        instance.save()
        return instance

class UserApiView(APIView):
    def get(self, request):
        print(request.data.get('email'))
        queryset = UsersAPI.objects.filter(email=request.data.get('email')).values().first()
        print(queryset)
        return Response("It is the return statement")

    def post(self, request):
        pass
