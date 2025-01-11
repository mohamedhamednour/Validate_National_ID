import unittest
from datetime import datetime
from .validation import NationalIDValidation
from .conf import EGYPT_GOVERNORATES

class TestNationalIDValidation(unittest.TestCase):
    def test_validate_national_id_valid(self):
        """Test a valid 14-digit national ID."""
        validator = NationalIDValidation("29901011501234")
        result = validator.validate_national_id()
        self.assertEqual(validator.errors, [])  

    def test_validate_national_id_invalid_length(self):
        """Test an invalid national ID with incorrect length."""
        validator = NationalIDValidation("123456789")
        result = validator.validate_national_id()
        self.assertIn('Invalid national ID: must be 14 digits', validator.errors)

    def test_calculate_first_digit_valid(self):
        """Test a valid first digit (2 or 3)."""
        validator = NationalIDValidation("29901011501234")
        validator.calculate_first_digit()
        self.assertEqual(validator.year, 1900)  

    def test_calculate_first_digit_invalid(self):
        """Test an invalid first digit (not 2 or 3)."""
        validator = NationalIDValidation("19901011501234")
        validator.calculate_first_digit()
        self.assertIn('First digit must be 2 or 3', validator.errors)

    def test_extract_birthdate_valid(self):
        """Test a valid birthdate extraction."""
        validator = NationalIDValidation("29901011501234")
        validator.calculate_first_digit()  
        validator.extract_birthdate()
        self.assertEqual(validator.birth_date, "1999-01-01")  

    def test_extract_birthdate_invalid(self):
        """Test an invalid birthdate extraction."""
        validator = NationalIDValidation("29999011501234") 
        validator.calculate_first_digit()  
        validator.extract_birthdate()
        self.assertIn('Invalid birthdate in national ID', validator.errors)
