from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm # 회원가입, 회원정보수정, 로그인
from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class CustomUserAuthenticationForm(AuthenticationForm):

    class Meta(AuthenticationForm):
        model = User
