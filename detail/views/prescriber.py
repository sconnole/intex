from django.conf import settings
from django_mako_plus import view_function, jscontext
from django import forms
import pyodbc
from django.http import HttpResponseRedirect
import http.client


@view_function
def process_request(request, param:str):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')
    
    if request.user.has_perm('account.search_all'):
        sql = ('''SELECT FullName, ''')
    else:
        sql = ('''SELECT NEWID(), ''')

    sql += (''' Gender, Credentials, State, Specialty FROM dbo.prescriber WHERE DoctorID = ?;''')
    docinfo = dSQL(sql, param)
    for item in docinfo:
        docname = item[0]
        docgender = item[1]
        doccred = item[2]
        docstate = item[3]
        docspecialty = item[4]

    sql = ('''SELECT Drug, Qty FROM triple WHERE DoctorID = ?;''')
    drugs = dSQL(sql, param)

    sql = ('''SELECT OpioidPerscriptionRatio FROM prescriber WHERE DoctorID = ?;''')
    ratio = dSQL(sql, param)
    for r in ratio:
        ratio = r[0]
    

    context = {
        "docname": docname,
        "docgender": docgender,
        "doccred": doccred,
        "docstate": docstate,
        "docspecialty": docspecialty,
        "drugs": drugs,
        "ratio": ratio,
    }
 
    return request.dmp.render('prescriber.html', context)


def dSQL (sql, param):
    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    return cursor.execute(sql, (param))


def convertParam (param):
    return "%" + param + "%"
