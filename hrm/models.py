import uuid

from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    GENDER = [
        ('N', 'Nam'),
        ('Nu', 'Nu'),
        ('K', 'Khac'),
    ]
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    email = models.EmailField()
    password = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    gender = models.CharField(max_length=10, choices=GENDER)
    address = models.TextField()

    def set_password(self, raw_password):
        self.password = make_password(password=raw_password, salt=None)
        self._password = raw_password
