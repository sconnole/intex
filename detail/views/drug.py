from django.conf import settings
from django_mako_plus import view_function, jscontext
from django import forms
import pyodbc
from django.http import HttpResponseRedirect


@view_function
def process_request(request, param:str):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')
    
    sql = ('''SELECT DrugName, IIF(IsOpioid = 0, 'Not an Opioid', 'Opioid') AS IsOpioid FROM dbo.opioids WHERE DrugName = ?;''')
    name_isop = dSQL(sql, param)
    for item in name_isop:
        drugname = item[0]
        isop = item[1]

    docs = []
    docids = []
    sql = ('''SELECT TOP(10) DoctorID FROM dbo.triple WHERE Drug = ? ORDER BY Qty DESC;''')
    pers = dSQL(sql, param)    
    sql = ('''SELECT FullName FROM prescriber WHERE DoctorID = ?;''')
    for per in pers:
        per = per[0]
        d = dSQL(sql, per)
        for doc in d:
            doc = doc[0]
        docs.append(doc)
        

    context = {
        "drugname": drugname,
        "isop": isop,
        "docs": docs,
        "docids": docids,
    }
 
    return request.dmp.render('drug.html', context)


def dSQL (sql, param):
    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    return cursor.execute(sql, (param))


def convertParam (param):
    return "%" + param + "%"
