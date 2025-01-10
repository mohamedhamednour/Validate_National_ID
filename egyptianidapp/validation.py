from datetime import datetime
import re
from .conf import EGYPT_GOVERNORATES
from django.core.exceptions import ValidationError


class NationalIDValidation:
    def __init__(self, id_number):
        self.id_number = str(id_number)  
        self.year = None
        self.birth_date = None
        self.code_governorate = None
        self.errors = [] 

    def validate_national_id(self):
        if not re.match(r'^\d{14}$', self.id_number):
            self.errors.append('Invalid national ID: must be 14 digits')

    def calculate_first_digit(self):
        if not self.errors:  
            print(self.id_number)
            first_digit = int(self.id_number[0])
            if first_digit not in {2, 3}: # 2 for 1900 to 1999, 3 for 2000 to 2099 
                self.errors.append('First digit must be 2 or 3')
            else:
                self.year = 1900 if first_digit == 2 else 2000

    def extract_birthdate(self):
        if not self.errors:  
            if not self.year:
                self.errors.append('Year not calculated. Call calculate_first_digit() first.')
            else:
                birthdate = self.id_number[1:7]
                date_str = f"{self.year + int(birthdate[0:2])}-{birthdate[2:4]}-{birthdate[4:6]}"
                self.birth_date = date_str
                try:
                    datetime.strptime(date_str, "%Y-%m-%d")
                except ValueError:
                    self.errors.append('Invalid birthdate in national ID')

    def check_governorates(self):
        if not self.errors: 
            code_governorate = self.id_number[7:9]
            self.code_governorate = code_governorate
            if code_governorate not in EGYPT_GOVERNORATES:
                self.errors.append('Invalid governorate code')

    def validate(self ):
        self.validate_national_id()
        self.calculate_first_digit()
        self.extract_birthdate()
        self.check_governorates()

        if self.errors:
            return {
                'status': 'invalid',
                'errors': self.errors
            }
            
       
        return {
                'status': 'valid',
                'birth_date': self.birth_date,
                'national_id':  self.id_number,
                'location': EGYPT_GOVERNORATES[self.code_governorate]
            }