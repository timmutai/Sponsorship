from account.models import account
from .serializer import studentSchoolSerializer
from student.models import applications
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

# captures student school info

# Apiview to handle cration of application and to retrieve list of applications
class  StudentSchoolInfo(APIView):
   authentication_classes = [ TokenAuthentication ]
   permission_classes = [IsAuthenticated]
   
  
   def get(self,request, format=None):
        user=applications.objects.all()
        serializer=studentSchoolSerializer(user, many=True)
      #   content={'students': serializer.data}
        return Response(serializer.data)
   
   def post(self, request, format=None):
      
      serializer = studentSchoolSerializer(data=request.data)
      
      if serializer.is_valid():
                
         
         serializer.save()
         
                    
         return Response(serializer.data)
      return Response(serializer.errors,)
     
  



  