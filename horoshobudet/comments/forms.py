from django.core.exceptions import ValidationError
from django.forms import HiddenInput
from django import forms
from captcha.fields import CaptchaField
from django.utils.deconstruct import deconstructible

from .models import Comment, ContactUs


class CommentForm(forms.ModelForm):
    """
    Форма для комментариев
    """
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'author': HiddenInput(),
            'comment': forms.Textarea(attrs={'class': 'comments-form-text',
                                             'placeholder': 'Минимум 5 символов, максимум - 500 символов.'}),
        }

    def clean_comment(self):
        comment = self.cleaned_data['comment']
        if len(comment) < 5:
            raise ValidationError('Текст должен содержать минимум 5 символов.')
        return comment


class ContactUsCreateForm(forms.ModelForm):
    """
    Форма отправки обратной связи
    """
    captcha = CaptchaField()

    class Meta:
        model = ContactUs
        fields = ('subject', 'email', 'text_mes')
        labels = {
            'email': 'Ваш почтовый ящик',
        }
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-input',
                                              'placeholder': 'Тема обращения'}),
            'email': forms.EmailInput(attrs={'class': 'form-input',
                                             'placeholder': 'На какой эл. адрес направить ответ'}),
            'text_mes': forms.Textarea(attrs={'cols': 73, 'rows': 10, 'class': 'form-input',
                                              'placeholder': 'Суть вопроса'}),
        }
