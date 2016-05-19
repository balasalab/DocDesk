from django import forms

from .models import SignUp

class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()

class SignUpForm(forms.ModelForm):
	"""docstring for SignUpForm"""
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']
		
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")
		if not domain == "gmail":
			raise forms.ValidationError("Please use a valid gmail address")
		return email
		pass

	def clean_full_name(self):
		full_name = self.cleaned_data.get("full_name")
		#write validation code
		return full_name
		pass