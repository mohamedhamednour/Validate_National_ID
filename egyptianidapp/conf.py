GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]





EGYPT_GOVERNORATES ={
    "01": "القاهرة",
    "02": "الإسكندرية",
    "03": "بورسعيد",
    "04": "السويس",
    "11": "دمياط",
    "12": "الدقهلية",
    "13": "الشرقية",
    "14": "القليوبية",
    "15": "كفر الشيخ",
    "16": "الغربية",
    "17": "المنوفية",
    "18": "البحيرة",
    "19": "الإسماعيلية",
    "21": "الجيزة",
    "22": "بني سويف",
    "23": "الفيوم",
    "24": "المنيا",
    "25": "أسيوط",
    "26": "سوهاج",
    "27": "قنا",
    "28": "أسوان",
    "29": "الأقصر",
    "31": "البحر الأحمر",
    "32": "الوادي الجديد",
    "33": "مطروح",
    "34": "شمال سيناء",
    "35": "جنوب سيناء"
}




class NationalIDValidation:
    
    def __init__(self, id_number):
        self.id_number = id_number
        self.year = None
    
    def validate_national_id(self):
        if not re.match(r'^\d{14}$', self.id_number):
            print('not valid')
            return ValidationError('Invalid national ID')
        
    def calculate_first_digit(self):
        d_str = str(self.id_number)
        first_digit = int(d_str[0])
        if first_digit < 2:
            ValidationError('First digit must be 2 or 3')
        self.year = 19 if first_digit == 2 else 20 if first_digit == 3 else None
    
    def extract_birthdate(self):
        
        card_str = str(self.id_number)
        birthdate = card_str[1:7]
        date_str = f"{self.year}{birthdate[0:2]}-{birthdate[2:4]}-{birthdate[4:6]}"
        try:
            return bool(datetime.strptime(date_str, "%Y-%m-%d"))
        except:
            return     ValidationError('First digit must be 2 or 3')

    
    def check_governorates(self):
        code_governorate = self.id_number[7:9]
        try:
            return code_governorate in EGYPT_GOVERNORATES
        except:
            return False

