from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.views import APIView
from django.core.exceptions import ValidationError

from .models import NationalID
from .serializers import NationalIDSerializer
from .validation import NationalIDValidation


class NationalIDViewSet(viewsets.ModelViewSet):
    queryset = NationalID.objects.all()
    serializer_class = NationalIDSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    permission_classes = [HasAPIKey]
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        number = request.data.get("number")
        existing_national_id = NationalID.objects.filter(number=number).first()
        if existing_national_id:
            serializer = self.get_serializer(existing_national_id)
            return Response(serializer.data, status=status.HTTP_200_OK)

        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'status': 'invalid', 'errors': e.message_dict}, status=status.HTTP_400_BAD_REQUEST)



class ValidateNationalIDAPIView(APIView):
    throttle_classes = [UserRateThrottle]
    permission_classes = [HasAPIKey]

    def post(self, request):
        id_number = request.data.get('id_number')

        if not id_number:
            return Response({'error': 'id_number is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validator = NationalIDValidation(id_number)
            result = validator.validate()

            if result.get('status') == 'invalid':
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            return Response(result, status=status.HTTP_200_OK)

        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
   

    
    
    
   



