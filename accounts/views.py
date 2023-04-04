from django.http import HttpResponse
from django.shortcuts import render
from .models import User

# Create your views here.

#Get all proucts for the releted User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductCountSerializer

class UserProductDetailView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductCountSerializer(user)
        return Response(serializer.data)



#Verify account view
def verify(request, email_token):
    try:
        obj = User.objects.get(email_token = email_token)
        obj.is_active = True
        obj.save()
        return HttpResponse("Your Account is now Verified")

    except Exception as e:
        return HttpResponse("Invalid token")
