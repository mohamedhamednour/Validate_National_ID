from . import validation
from django_lifecycle import LifecycleModelMixin, BEFORE_CREATE, hook
from .serviceapp import generate_random_14_digit_number
from datetime import timedelta
from .validation import NationalIDValidation
from django.core.exceptions import ValidationError
from .conf import EGYPT_GOVERNORATES

class NationalIDMixin(LifecycleModelMixin):

    @hook(BEFORE_CREATE)
    def generate_id_for_number(self):
        print('generate_id_for_number')
        validator = NationalIDValidation(self.number)
        validation_result = validator.validate()

        if validation_result['status'] == 'invalid':
            raise ValidationError({'number': validation_result['errors']})

        self.birth_date = validator.birth_date
        self.location = EGYPT_GOVERNORATES[validator.code_governorate]


