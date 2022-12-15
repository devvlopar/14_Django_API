from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from . serializers import Serializing
from rest_framework.response import Response
# Create your views here.

class UserGet(APIView):
    def get(self,request):
        all_users = User.objects.all()
        all_data_obj = Serializing(all_users, many = True)
        return Response(all_data_obj.data)

class UserCreate(APIView):
    def post(self, request):
        all_data_obj = Serializing(data = request.data)
        if all_data_obj.is_valid():
            all_data_obj.save()
            all_users = User.objects.all()
            all_data_obj = Serializing(all_users, many = True)
            return Response(all_data_obj.data)
        else:
            return Response(all_data_obj.errors)


class PutUser(APIView):
    def put(self, request, pk):
        user_row = User.objects.get(id = pk)
        data_obj = Serializing(user_row, data= request.
        data)
        if data_obj.is_valid():
            data_obj.save()
            all_users = User.objects.all()
            all_data_obj = Serializing(all_users, many = True)
            return Response(all_data_obj.data)
        else:
            return Response(data_obj.errors)


class DeleteUser(APIView):
    def delete(self, request, pk):
        u_obj = User.objects.get(id= pk)
        u_obj.delete()
        all_users = User.objects.all()
        all_data_obj = Serializing(all_users, many = True)
        return Response(all_data_obj.data)
        