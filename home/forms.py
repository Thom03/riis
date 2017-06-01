from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from home.models import Contact
from django import forms
from django.forms import ModelForm, Textarea



from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

class RegistrationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.layout = Layout(
			'username',
			'password1',
			'password2',

			ButtonHolder(
				Submit('register', 'Register', css_class='btn-success')
			)
		)


class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.layout = Layout(
			'username',
			'password',
			ButtonHolder(
				Submit('login', 'Login', css_class='btn-success')
			)
		)		


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['full_name', 'email', 'message']

		widgets = {
            'message': Textarea(attrs={'cols': 15, 'rows': 20}),
        }

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name
	def clean_email(self):
		email = self.cleaned_data.get('email')
		return email		

