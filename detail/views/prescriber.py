from django.conf import settings
from django_mako_plus import view_function, jscontext
from django import forms
import pyodbc
from django.http import HttpResponseRedirect
import requests


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


    ##########################################################
    # Azure Analytics related prescribers
    url = "https://ussouthcentral.services.azureml.net/workspaces/a6a8851e6a794d0ab9b2221bf735138c/services/b03ef81972164572a7a19b5449bc2ccb/execute"

    querystring = {"api-version":"2.0","details":"true%0A%0A"}

    payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"DoctorID\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"" + param + "\"\r\n        ]\r\n      ]\r\n    }\r\n  },\r\n  \"GlobalParameters\": {}\r\n}\r\n"
    headers = {
        'Authorization': "Bearer cNJh04G7zR3xZJKcJVvKH7lCA16NGsDm+UWre322zqJSy/sz3wOJQiOt4yQIBnyjUiPPNbh0EzCv2N1fpeY39Q==",
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "1d0d2bf5-074f-43d2-94b5-afaf7fe41307"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    jr = response.json()

    jr = jr["Results"]["output1"]["value"]["Values"]
    p1 = jr[0][1]
    p2 = jr[0][2]
    p3 = jr[0][3]
    p4 = jr[0][4]
    p5 = jr[0][5]

    if request.user.has_perm('account.search_all'):
        sql = ('''SELECT CONCAT(Fname, ' ', Lname), ''')
    else:
        sql = ('''SELECT NEWID(), ''')

    sql += ('''DoctorID FROM prescriber WHERE DoctorID in (?, ?, ?, ?, ?);''')

    relusers = uSQL(sql, p1, p2, p3, p4, p5)
    ##########################################################
    

    context = {
        "docname": docname,
        "docgender": docgender,
        "doccred": doccred,
        "docstate": docstate,
        "docspecialty": docspecialty,
        "drugs": drugs,
        "ratio": ratio,
        "relusers": relusers,
    }
 
    return request.dmp.render('prescriber.html', context)


def dSQL (sql, param):
    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    return cursor.execute(sql, (param))

def uSQL (sql, p1, p2, p3, p4, p5):
    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    return cursor.execute(sql, (p1, p2, p3, p4, p5))


def convertParam (param):
    return "%" + param + "%"
