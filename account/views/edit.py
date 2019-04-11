from django.conf import settings
from django_mako_plus import view_function
from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
import pyodbc

@view_function
def process_request(request, docID:int=0):
    if not request.user.has_perm('account.change_user'):
        return HttpResponseRedirect('/account/permission_denied/') 
    
    sql = ('''SELECT FullName, Gender, Credentials, State, Specialty, DoctorID  
            FROM dbo.prescriber 
            WHERE DoctorID = ?
           ''')

    docs = runSQL(sql, (docID))
    
    for item in docs: 
        doctor = item

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
        "doctor": doctor,
    }

    return request.dmp.render('edit.html', context)

class PrescriberForm(forms.Form):
    gender = forms.ChoiceField(choices=[("M", "Male"), ("F", "Female"),])
    location = forms.CharField(label="Location", max_length=2)
    credentials = forms.CharField(label="Credentials")
    specialty = forms.CharField(label="Specialty")

def runSQL (sql, param):
    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    return cursor.execute(sql, (param))