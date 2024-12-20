from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model =CustomUser
        fields = ('username','last_name','first_name' ,  'age')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model =CustomUser
        fields = ('username', 'last_name', 'first_name' , 'age')    