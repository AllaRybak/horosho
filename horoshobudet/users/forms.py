from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.core.exceptions import ValidationError

from users.models import TagMaster


class LoginUserForm(AuthenticationForm):
    """
    Форма для login
    """
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                            'placeholder': 'Логин или email'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    """
    Форма для регистрации пользователя
    """
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(required=True, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже используется.")
        return email


class ProfileUserForm(forms.ModelForm):
    """
    Форма для аккаунта пользователя
    """
    this_year = datetime.now().year
    date_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year - 80, this_year - 5))))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'date_birth',  'phone_number', 'photo',
                  'is_master', 'tags', 'content',]
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'date_birth': 'Дата рождения',
            'is_master': 'Я мастер, предлагаю услуги',
            'content': 'Обо мне',
            'tags': 'Навыки',
            'phone_number': 'Телефон',
            'photo': 'Фото (аватар)',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'date_birth': forms.DateInput(attrs={'class': 'form-input'}),
            'is_master': forms.CheckboxInput(attrs={'class': 'form-input-is_master'}),
            'content': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Максимум 800 символов'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input'}),
            'photo': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileUserForm, self).__init__(*args, **kwargs)
        self.fields["tags"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["tags"].help_text = ""
        self.fields["tags"].queryset = TagMaster.objects.all()

    def clean_content(self):
        content = self.cleaned_data['content']
        master = self.cleaned_data['is_master']
        if master and not content:
            raise ValidationError("Поле обязательно для заполнения.")
        return content


class UserPasswordChangeForm(PasswordChangeForm):
    """
    Форма для смены пароля
    """
    old_password = forms.CharField(label="Старый пароль",
                                   widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label="Новый пароль",
                                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label="Подтвердите",
                                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))
