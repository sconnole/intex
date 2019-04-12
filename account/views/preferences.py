from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from account.models import User
from django.http import HttpResponse, HttpResponseRedirect

@view_function
def process_request(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')
    if request.method == 'POST':
        form = UpdatepreferenceForm(request.POST)
        form.is_valid()
        
    else:
        form = UpdatepreferenceForm()

    context = {
        'form': form,
    }
    return request.dmp.render('/account/templates/preferences.html', context)

class UpdatepreferenceForm(forms.Form):
    password = forms.CharField(label=u'Password', widget=forms.PasswordInput())
    confirmpassword = forms.CharField(label=u'Confirm Password', widget=forms.PasswordInput())
                        
    def clean(self):
        if (self.cleaned_data.get('password') != self.cleaned_data.get('confirmpassword')):
            raise ValidationError('Passwords do not match')
        return self.cleaned_datadata