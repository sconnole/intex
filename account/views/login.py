from django.conf import settings
from django_mako_plus import view_function
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from account.models import User
from django.http import HttpResponse, HttpResponseRedirect

@view_function
def process_request(request):
    request.session.flush()
    if request.method == 'POST':
        
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(request, username=form["username"].value(), password=form["password"].value())
            login(request, user)
            return HttpResponseRedirect('/homepage/index/')
        else:
            pass

    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return request.dmp.render('/account/templates/login.html', context)

class LoginForm(forms.Form):
    username = forms.CharField(label=u'Username', max_length=30)
    password = forms.CharField(
                                label=u'Password',
                                widget=forms.PasswordInput()
                                )
    def clean(self):
        data = self.cleaned_data
        user = authenticate(username=data.get("username"), password=data.get("password"))
        if user is None:
            raise ValidationError('Invalid username or password.')
        return data