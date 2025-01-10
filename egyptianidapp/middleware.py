import json
from django.utils import timezone
from .models import NationalIDLog

class NationalIDLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in ['/api/v1/national-id/', '/api/v2/national-id/']:
            request_body = {}
            if request.method in ['POST', 'PUT', 'PATCH']:
                try:
                    request_body = json.loads(request.body.decode('utf-8'))
                except json.JSONDecodeError:
                    request_body = {}

            response = self.get_response(request)   
            NationalIDLog.objects.create(
                endpoint=request.path,
                method=request.method,
                status_code=response.status_code,
                request_data=request_body,
                timestamp=timezone.now(),
            )

            return response
        else:
            return self.get_response(request)

