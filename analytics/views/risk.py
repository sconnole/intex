from django.conf import settings
from django_mako_plus import view_function, jscontext
from django.http import HttpResponseRedirect
from datetime import datetime, timezone
import pyodbc


ROWS = 50
OFFSET = 0
@view_function
def process_request(request, page:int=0):
    if not request.user.has_perm('account.view_analytics'):
        return HttpResponseRedirect('/account/permission_denied/')

    OFFSET = page * ROWS 

    sql = ('''SELECT FullName, TRAMADOL_HCL, CEPHALEXIN, LEVOFLOXACIN, GABAPENTIN, METHADONE_HCL, SULFAMETHOXAZOLE_TRIMETHOPRIM, HYDROCHLOROTHIAZIDE, TotalPrescriptions,
	        cast((TRAMADOL_HCL + CEPHALEXIN + LEVOFLOXACIN +  GABAPENTIN +  METHADONE_HCL +  SULFAMETHOXAZOLE_TRIMETHOPRIM +  HYDROCHLOROTHIAZIDE) / TotalPrescriptions as decimal(10,3)) as similar_sum 	
            FROM prescriber
            WHERE Opioid_Prescriber = 0 and TotalPrescriptions > 0
            order by similar_sum desc
            OFFSET ? ROWS
            FETCH NEXT ? ROWS ONLY;
        ''')
    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    docs = cursor.execute(sql,(OFFSET, ROWS))   

    context = { 
        "docs": docs,
        "page":page
    }
    return request.dmp.render('risk.html', context)