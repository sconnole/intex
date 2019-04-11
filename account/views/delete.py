from django.conf import settings
from django_mako_plus import view_function, jscontext
import pyodbc
from django.http import HttpResponseRedirect

@view_function
def process_request(request,  docID:int=0):
    if not request.user.has_perm('account.delete_user'):
        return HttpResponseRedirect('/account/permission_denied/') 

    sql = ('''SELECT FullName, Gender, Credentials, State, Specialty, DoctorID  
            FROM dbo.prescriber 
            WHERE DoctorID = ?
           ''')

    docs = runSQL(sql, (docID))

    for item in docs:
        doctor = item

    context = {
        "doctor": doctor
    }

    return request.dmp.render('delete.html', context)

def runSQL (sql, param):
    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    return cursor.execute(sql, (param))