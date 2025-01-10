
from django.db import models
from django.db.models import QuerySet

class NationalIDManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
            status=models.Case(
                models.When(number__isnull=False, then=models.Value('valid')),
                default=models.Value('invalid')
            )
        )


