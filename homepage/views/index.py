from django.conf import settings
from django_mako_plus import view_function, jscontext
from django import forms
import pyodbc
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Permission

ROWS = 5
OFFSET = 0

@view_function
def process_request(request, page:int=0):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')

    OFFSET = page*ROWS
    if request.method == "POST": 
        request.session['param'] = convertParam(request.POST['search'])
    
    if 'param' in request.session:
        param = request.session['param'] 
    else:
        param = ""

    if request.user.has_perm('account.search_all'):
        sql = ('''SELECT FullName, ''')
    else:
        sql = ('''SELECT NEWID(), ''')
    
    sql += (''' Gender, Credentials, State, Specialty  
            FROM dbo.prescriber 
            WHERE Lname LIKE ?
            OR Fname LIKE ?
            OR Gender LIKE ?
            OR Credentials LIKE ?
            OR state LIKE ?
            OR Specialty LIKE ?
            ORDER BY FullName 
            OFFSET ? ROWS
            FETCH NEXT ? ROWS ONLY;
        ''')
    docs = pSQL(sql, param, OFFSET)
    
    sql = ('''SELECT DrugName, IIF (
            IsOpioid = '0', 'No', 'Yes'
            ) AS 'Opioid' 
        FROM dbo.opioids
        WHERE DrugName LIKE ?
        OR IsOpioid LIKE ?
        ORDER BY DrugName
        OFFSET ? ROWS
        FETCH NEXT ? ROWS ONLY;''')

    drugs = dSQL(sql, param, OFFSET)

    context = {
        "prescribers": docs,
        "drugs": drugs,
        "page": page,
        "form": SearchForm()
    }
 
    return request.dmp.render('index.html', context)

def pSQL (sql, param, offset):
    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    return cursor.execute(sql, (param, param, param, param, param, param, offset, ROWS))

def dSQL (sql, param, offset):
    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    return cursor.execute(sql, (param, param, offset, ROWS))


def convertParam (param):
    return "%" + param + "%"

class SearchForm(forms.Form):
    search = forms.CharField(label=u'',
        widget=forms.TextInput(attrs={'placeholder': 'Search...', 'id':'mySearch'}))

        
