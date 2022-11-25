import uuid

from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    GENDER = [
        ('M', 'Nam'),
        ('W', 'Nu'),
        ('O', 'Khac'),
    ]
    ROLE = [
        ('AD', 'Admin'),
        ('US', 'User')
    ]
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=60, default=make_password('1234', salt=None))
    name = models.CharField(max_length=60)
    gender = models.CharField(max_length=10, choices=GENDER)
    address = models.TextField()
    role = models.CharField(max_length=10, choices=ROLE, default='US')

    def set_password(self, raw_password):
        self.password = make_password(password=raw_password, salt=None)
        self._password = raw_password
