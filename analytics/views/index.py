from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
import pyodbc
import http.client
import itertools
import requests



ROWS = 50
OFFSET = 0

@view_function
def process_request(request, page:int=0):


    OFFSET = page * ROWS

    sql = ('''Select fullname, Specialty, OpioidPerscriptionRatio 
            from prescriber 
            where Opioid_Prescriber = 1
            AND OpioidPerscriptionRatio > 80 
            AND Specialty not like '%Surg%' 
            order by OpioidPerscriptionRatio desc
            OFFSET ? ROWS
            FETCH NEXT ? ROWS ONLY;
        ''')
    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    docs = cursor.execute(sql,(OFFSET, ROWS))
    

    conn2 = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn2.cursor()


    psql = ('''Select fullname, doctorID
            from prescriber 
            where Opioid_Prescriber = 1
            AND OpioidPerscriptionRatio > 80 
            AND Specialty not like '%Surg%' 
            order by fullname asc
        ''')
    
    result = cursor.execute(psql)   

    if request.method == "POST": 
            

        url = "https://ussouthcentral.services.azureml.net/workspaces/a6a8851e6a794d0ab9b2221bf735138c/services/b03ef81972164572a7a19b5449bc2ccb/execute"

        querystring = {"api-version":"2.0","details":"true%0A%0A"}

        payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"DoctorID\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"" + request.POST["doctorID"] + "\"\r\n        ]\r\n      ]\r\n    }\r\n  },\r\n  \"GlobalParameters\": {}\r\n}\r\n"
        headers = {
            'Authorization': "Bearer cNJh04G7zR3xZJKcJVvKH7lCA16NGsDm+UWre322zqJSy/sz3wOJQiOt4yQIBnyjUiPPNbh0EzCv2N1fpeY39Q==",
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "1d0d2bf5-074f-43d2-94b5-afaf7fe41307"
            }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

        response = str(response.text[60:])
        response = response[response.find( '"', 1 ) + 2:]
        response = response.replace('"', '').replace(']', '').replace('}', '')

        relatedpers = response.split(',')

        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print(response)


        # sql2 = {'''select fullname from prescriber where DoctorID like 1003120502''' }
        # relatedpers = curser.execute(sql2)
        

    context = { 
        "prescribers": docs,
        "result": result, 
        "relatedpers":relatedpers

    }
    return request.dmp.render('index.html', context)


  
  



  