from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       
       read_only_fields = ('pk','')
       fields = ('phone','get_full_name','id','email', 'first_name', 'last_name','role','username','gender','is_staff')