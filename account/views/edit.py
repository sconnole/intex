from django.conf import settings
from django_mako_plus import view_function
from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
import pyodbc

@view_function
def process_request(request, docID:int=0):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')
    if not request.user.has_perm('account.change_user'):
        return HttpResponseRedirect('/account/permission_denied/') 
    
    sql = ('''SELECT FullName, Gender, Credentials, State, Specialty, DoctorID  
            FROM dbo.prescriber 
            WHERE DoctorID = ?
           ''')

    docs = runSQL(sql, (docID))

    for item in docs:
        doctor = item
 
    # Update DB
    # Redirect to this page, but with updated data showing

    if request.method == 'POST':
        location = request.POST['location']
        credentials = request.POST['credentials']
        specialty = request.POST['specialty']
        gender = request.POST['gender']

        sql = ('''UPDATE prescriber
                SET 
                    Gender = ?, 
                    State = ?, 
                    Credentials = ?, 
                    Specialty = ?
                WHERE DoctorID = ?; ''')
        conn = pyodbc.connect(settings.CONNECTION_STRING)
        cursor = conn.cursor()
        cursor.execute(sql, (gender, location, credentials, specialty, docID ))
        conn.commit()
        return HttpResponseRedirect('/account/edit/{}'.format(docID))

    form = PrescriberForm(initial={'gender': doctor[2], 'location': doctor[3], 'credentials': doctor[2], 'specialty': doctor[4]})

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