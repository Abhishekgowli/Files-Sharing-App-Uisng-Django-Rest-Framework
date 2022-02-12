from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import FileListSeralizer
from rest_framework.response import Response

# Create your views here.

class HandelFileUpload(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=FileListSeralizer(data=data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':200,
                    'message':'files uploaded successfully'
                })
            return Response({
                    'status':400,
                    'message':'someting went wrong',
                    'data':serializer.errors
                })
        except Exception as e:
            print(e)




def home(request):
    return render(request,'home.html')