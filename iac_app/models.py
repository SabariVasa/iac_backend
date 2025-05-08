from mongoengine import Document, StringField, EmailField
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password, check_password

class User(Document):
    username = StringField(required=True, unique=True, max_length=50)
    phone_number = StringField(
        required=True,
        unique=True,
        regex=r'^\+?\d{10,15}$'
    )
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
