from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):  
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}) 
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}) 
    )

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("As senhas não coincidem.")

class CreatePipeForm(forms.Form):
    name = forms.CharField(label='Pipe Name', max_length=100)

class UpdatePipeForm(forms.Form):
    name = forms.CharField(label='New Pipe Name', max_length=100)

class CreatePhaseForm(forms.Form):
    name = forms.CharField(label='Phase Name')

class CreateCardForm(forms.Form):   
    title = forms.CharField(label='Card Title')

class UpdateCardForm(forms.Form):
    title = forms.CharField(label='New Card Title', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))