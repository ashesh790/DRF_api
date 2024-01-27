from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from termcolor import colored
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import * 
from .serializers import * 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def index(request, format=None):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    data = Student.objects.all()
    ser_data = student_ser(data, many = True)
    return Response({'status': 200, 'payload' : ser_data.data})

@api_view(['POST'])
def post_data(request): 
    ser_data = student_ser(data = request.data)
    print(ser_data)
    if not ser_data.is_valid():
        print(ser_data.errors)
        return Response({'status': 403, 'message': ser_data.errors})
    ser_data.save()
    return Response({'status': 200, 'payload' : ser_data.data, 'message': "Data Saved!"})

@api_view(['PUT'])
def update_put_data(request, id):
    try:
        ser_data = Student.objects.get(id = id)
        ser_data = student_ser(ser_data, data = request.data)
        print(ser_data)
        if not ser_data.is_valid():
            print(ser_data.errors)
            return Response({'status': 403, 'message': ser_data.errors})
        ser_data.save()
        return Response({'status': 200, 'payload' : ser_data.data, 'message': "Data Saved!"})
    except Exception as ex: 
        print(ex)
        return Response({"status": 403, "message": "Invalid id"})

@api_view(['PATCH'])
def update_patch_data(request, id):
    try:
        ser_data = Student.objects.get(id = id)
        ser_data = student_ser(ser_data, data = request.data, partial = True)
        print(ser_data)
        if not ser_data.is_valid():
            print(ser_data.errors)
            return Response({'status': 403, 'message': ser_data.errors})
        ser_data.save()
        return Response({'status': 200, 'payload' : ser_data.data, 'message': "Data Saved!"})
    except Exception as ex: 
        print(ex)
        return Response({"status": 403, "message": "Invalid id"}) 

@api_view(['DELETE'])
def delete_data_record(request, id):
    try:
        ser_data = Student.objects.get(id = id)
        ser_data.delete()
        return Response({'status': 200, 'message': "Data Deleted!"})
    except Exception as ex: 
        # print(colored('hello', 'red'), colored('world', 'green'))
        print(colored(ex, 'red'))
        return Response({"status": 403, "message": "Invalid id"})
    

@api_view(['GET'])
def book_data(request): 
    data = Book.objects.all() 
    ser_data = book_ser(data, many = True) 
    return Response({'status': 200, 'payload': ser_data.data})


class register_user(APIView):
    def post(self, request): 
        ser_data = user_ser(data = request.data)

        if not ser_data.is_valid(): 
            print(ser_data.errors)
            return Response({'status': 403, 'message': "Not valid!"})
        ser_data.save()
        user = User.objects.get(username = ser_data.data['username'])
        token_obj, _ = Token.objects.get_or_create(user=user)
        return Response({'status': 200, 'payload': ser_data.data, 'token':str(token_obj), 'message': "Valid!"})
        

