from django import forms

class AuthenticationForm(forms.Form):
    """
    Login form
    """
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))

    class Meta:
        fields = ['username', 'password']