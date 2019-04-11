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

    sql = ('''SELECT DrugName, IIF(IsOpioid = 0, 'Not an Opioid', 'Opioid') AS IsOpioid
                FROM dbo.opioids WHERE DrugName = ?;''')
    name_isop = dSQL(sql, param)
    for item in name_isop:
        drugname = item[0]
        isop = item[1]
    
    # param = param.replace('.', '_')

    sql = ('''SELECT TOP(10) 
                (SELECT FullName 
                FROM prescriber AS p 
                WHERE p.DoctorID = t.DoctorID) AS FullName, 
                DoctorID, Qty 
            FROM triple AS t 
            WHERE Drug = ?
            ORDER BY Qty DESC;''')

    docs = dSQL(sql, param) 

    ##########################################################
    # Azure Analytics drugs prescribed with this one
    url = "https://ussouthcentral.services.azureml.net/workspaces/a6a8851e6a794d0ab9b2221bf735138c/services/7e6fef0270ad40c3a05aa3b3de4ebfd1/execute"

    querystring = {"api-version":"2.0","details":"true"}

    payload = "{\n  \"Inputs\": {\n    \"input1\": {\n      \"ColumnNames\": [\n        \"Drug\"\n      ],\n      \"Values\": [\n        [\n          \"" + param + "\"\n        ]\n      ]\n    }\n  },\n  \"GlobalParameters\": {}\n}"
    headers = {
        'Authorization': "Bearer BL0ofc/KWATjpIzJCVleg4Fe73Y0m2bnz8wcd7IGcKfEplxgC0MzjAzL6bQa+xwtTU9RdHA/u2ffYktjEmJ8Xw==",
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "2ef6170b-117d-4eee-a2dd-93405a7bde71"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    response = str(response.text[236:])
    response = response[response.find( '"', 1 ) + 2:]
    response = response.replace('"', '').replace(']', '').replace('}', '')

    reldrugs = response.split(',')
    ##########################################################
    

    context = {
        "drugname": drugname,
        "isop": isop,
        "docs": docs,
        "reldrugs": reldrugs,
    }
 
    return request.dmp.render('drug.html', context)


def dSQL (sql, param):
    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    return cursor.execute(sql, (param))

def SQL (sql):
    con = pyodbc.connect(settings.CONNECTION_STRING)
    cur = con.cursor()
    return cur.execute(sql)
