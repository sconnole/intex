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
    

    sql = ('''SELECT FullName, Gender, Credentials, State, Specialty FROM dbo.prescriber WHERE DoctorID = ?;''')
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
    # Azure Analytics drugs prescribed with this one
    # conn = http.client.HTTPConnection("ussouthcentral,services,azureml,net")

    # payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"DoctorID\",\r\n        \"Drug\",\r\n        \"LnPlus1(Qty)\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"0\",\r\n          \"" + param + "\",\r\n          \"0\"\r\n        ]\r\n      ]\r\n    }\r\n  },\r\n  \"GlobalParameters\": {}\r\n}"
    # headers = {
    #     'Authorization': "Bearer BL0ofc/KWATjpIzJCVleg4Fe73Y0m2bnz8wcd7IGcKfEplxgC0MzjAzL6bQa+xwtTU9RdHA/u2ffYktjEmJ8Xw==",
    #     'Content-Type': "application/json",
    #     'cache-control': "no-cache",
    #     'Postman-Token': "eb7ea9c0-8a05-4a6e-af3f-08d65339f982"
    #     }

    # conn.request("POST", "workspaces,a6a8851e6a794d0ab9b2221bf735138c,services,7e6fef0270ad40c3a05aa3b3de4ebfd1,execute", payload, headers)

    # res = conn.getresponse()
    # data = res.read()

    # print(data.decode("utf-8"))
    ##########################################################
    

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
