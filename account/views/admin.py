from django.conf import settings
from django_mako_plus import view_function
from homepage.views.index import SearchForm
from django.http import HttpResponseRedirect
import pyodbc

ROWS = 10
OFFSET = 0

@view_function
def process_request(request, page:int=0):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')
    if not request.user.has_perm('account.add_user'):
        return HttpResponseRedirect('/account/permission_denied/') 

    OFFSET = page * ROWS
    if request.method == "POST": 
        request.session['admin_search'] = convertParam(request.POST['search'])
    
    if 'admin_search' in request.session:
        param = request.session['admin_search'] 
    else:
        param = "default"
    
    sql = ('''SELECT FName, LName, DoctorID  
            FROM dbo.prescriber 
            WHERE Lname LIKE ? 
            OR Fname LIKE ? 
            ORDER BY LName
            OFFSET ? ROWS
            FETCH NEXT ? ROWS ONLY
    ;''')

    docs = dSQL(sql, param, OFFSET)

    context = {
        "form": SearchForm(),
        "docs": docs,
        "page": page
    }

    return request.dmp.render('admin.html', context)

def convertParam (param):
    param = param.replace('%', '\%').replace('[', '\[').replace(']', '\[')
    return "%" + param + "%"

def dSQL (sql, param, offset):
    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    return cursor.execute(sql, (param, param, offset, ROWS))