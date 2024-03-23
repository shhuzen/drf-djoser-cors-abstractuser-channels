from django.db import models
from django.contrib.auth.models import  AbstractUser

class User(AbstractUser):
 GENDER_CHOICES = [
        ('Муж', 'Муж'),
        ('Жен', 'Жен'),
    ]

 USERNAME_FIELD = 'username'
 gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
    )
 phone = models.CharField(max_length=20, null= True, blank= True)
 REQUIRED_FIELDS = ['phone'] # если нужно добавить что то в djoser /users/me endpoint нужно в массив добавить
 
 
# перпеписка встроенного метода для админки django и для фротндэнда  при изменение пароля 
#  def save(self, *args, **kwargs):     
#           self.set_password(self.password)
#           super().save(*args, **kwargs)