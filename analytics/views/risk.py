from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
import pyodbc


ROWS = 50
OFFSET = 0
@view_function
def process_request(request, page:int=0):

    OFFSET = page * ROWS 

    sql = ('''SELECT FullName, TRAMADOL_HCL, CEPHALEXIN, LEVOFLOXACIN, GABAPENTIN, METHADONE_HCL, SULFAMETHOXAZOLE_TRIMETHOPRIM, HYDROCHLOROTHIAZIDE
            FROM prescriber
            WHERE Opioid_Prescriber = 0
            order by fullname
            OFFSET ? ROWS
            FETCH NEXT ? ROWS ONLY;
        ''')
    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    docs = cursor.execute(sql,(OFFSET, ROWS))   


    score = docs[0] 
    

    context = { 
        "docs": docs,
        "page":page
    }
    return request.dmp.render('risk.html', context)


  
  


