from django.conf import settings
from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect
import pyodbc

@view_function
def process_request(request, docID:int=0):
    if not request.user.has_perm('account.add_user'):
        return HttpResponseRedirect('/account/permission_denied/') 
    
    # Query current data of docID
    # Display that data
    # Clean data? 
    # if request.method == POST: 
    # Check for valid form
    # Update DB
    # Redirect to this page, but with updated data showing

    form = PrescriberForm()

    context = {
        "form": form,
    }

    return request.dmp.render('edit.html', context)

class PrescriberForm(forms.Form):
    gender = forms.ChoiceField(choices=[("M", "Male"), ("F", "Female"),])
    location = forms.CharField(label="Location")
    credentials = forms.CharField(label="Credentials")
    specialty = forms.CharField(label="Specialty")