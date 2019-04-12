from django.conf import settings
from django_mako_plus import view_function, jscontext
import pyodbc
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')
    if not request.user.has_perm('account.delete_user'):
        return HttpResponseRedirect('/account/permission_denied/') 
    
    docID = request.POST['doctorID']

    sql = ('''DELETE FROM prescriber WHERE DoctorID = ?''')
    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    cursor.execute(sql, (docID))
    cursor.commit()

    return HttpResponseRedirect('/account/admin/')
