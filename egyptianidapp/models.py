from django.db import models
from .mixinmodels   import NationalIDMixin
from .manager import NationalIDManager
# Create your models here.


class NationalID(NationalIDMixin ,models.Model):
    number = models.CharField(max_length=14, unique=True)
    birth_date = models.DateField(null=True)
    location = models.CharField(max_length=100, null=True , blank=True)
    objects: NationalIDManager = NationalIDManager()

 
    class Meta:
        verbose_name = 'National ID'
        verbose_name_plural = 'National IDs'
        

    def __str__(self):
        return self.number


class NationalIDLog(models.Model):
    endpoint = models.CharField(max_length=255)  
    method = models.CharField(max_length=10)  
    status_code = models.PositiveIntegerField()  
    response_data = models.JSONField(blank=True, null=True , default=dict) 
    request_data = models.JSONField(blank=True, null=True, default=dict)  # إضافة حقل request_data
    timestamp = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.method} {self.endpoint} ({self.status_code})"

