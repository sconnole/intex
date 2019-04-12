from django.conf import settings
from django_mako_plus import view_function
from account.views.edit import PrescriberForm
from django import forms
from django.http import HttpResponseRedirect
import pyodbc

@view_function
def process_request(request, docID:int=0):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')
    if not request.user.has_perm('account.add_user'):
        return HttpResponseRedirect('/account/permission_denied/') 

    if request.method == 'POST':
        first = request.POST['FName']
        last = request.POST['LName']
        location = request.POST['location']
        credentials = request.POST['credentials']
        specialty = request.POST['specialty']
        gender = request.POST['gender']
        fullname = last + ', ' + first

        sql = ('''INSERT INTO prescriber (Fname, Lname, FullName, Gender, State, Credentials, Specialty)
                VALUES (? , ? , ?, ? , ? , ?, ?); ''')
        conn = pyodbc.connect(settings.CONNECTION_STRING)
        cursor = conn.cursor()
        cursor.execute(sql, (first, last, fullname, gender, location, credentials, specialty ))
        conn.commit()
        return HttpResponseRedirect('/account/admin')


    form = addPrescriber()

    context = {
        "form": form,
    }

    return request.dmp.render('add.html', context)

class addPrescriber(PrescriberForm):
    FName = forms.CharField(label="First Name")
    LName = forms.CharField(label="Last Name")



