from accounts.models import User
from django import forms
from django.contrib.auth import password_validation


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        strip=True,
        validators=[password_validation.validate_password],
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already being used.')
        return username

    def save(self, commit=True):
        instance = super(RegisterForm, self).save(commit=False)
        instance.set_password(instance.password)
        instance.is_active = True
        instance.save() if commit else None
        return instance

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
