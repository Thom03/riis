from __future__ import absolute_import

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import generic
from home.forms import RegistrationForm, LoginForm, ContactForm


from django.contrib.auth.decorators import login_required

from braces import views

# Create your views here.
def index(request):
	return render (request, "index.html", {})



	
class About(TemplateView):
	template_name = "about.html"

class SignUpView(views.AnonymousRequiredMixin,views.FormValidMessageMixin, generic.CreateView):
	form_class = RegistrationForm
	form_valid_message = 'Thanks for Signing up, go ahead and LogIn'
	model = User
	template_name = 'signup.html'

class LoginView(views.AnonymousRequiredMixin,views.FormValidMessageMixin, generic.FormView):
	form_class = LoginForm
	form_valid_message = 'You are logged in now.'
	success_url = reverse_lazy('home')
	template_name = 'login.html'

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)

		if user is not None and user.is_active:
			login(self.request, user)
			return super(LoginView, self).form_valid(form)
		else:
			return self.form_invalid(form)	

class LogOutView(views.LoginRequiredMixin, views.MessageMixin, generic.RedirectView):
	url = reverse_lazy('home')



	def get(self, request, *args, **kwargs):
		logout(request)
		self.messages.success("You've been logged out. Come back soon!")
		return  super(LogOutView, self).get(request, *args, **kwargs)



def contact(request):
	title = 'Contact Us'
	form = ContactForm(request.POST or None)
	if form.is_valid():
		instance = form.save()
		print form.cleaned_data

	context = {
	"form": form,
	"title": title,

	}
	return render(request, "faq.html", context)