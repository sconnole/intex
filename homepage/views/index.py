from django.conf import settings
from django_mako_plus import view_function, jscontext

@view_function
def process_request(request):
    
    #check if search occured 
    #clean input
    #return results 

    sql = ("SELECT FullName, Gender, Credentials, State, Specialty "
    " FROM dbo.prescriber"
    " ORDER BY Lname"
    " OFFSET 0 ROWS"
    " FETCH NEXT 5 ROWS ONLY;")

    results = runSql(sql)
    docs = []
    for row in results:
        docs.append(row)
    sql = ("SELECT DrugName, IsOpioid "
    " FROM dbo.opioids"
    " ORDER BY DrugName"
    " OFFSET 0 ROWS"
    " FETCH NEXT 5 ROWS ONLY;")

    results = runSql(sql)
    drugs = []
    for row in results: 
        drugs.append(row)

    context = {
        "prescribers": docs,
        "drugs": drugs
    }

    return request.dmp.render('index.html', context)
    
def runSql (sql): 
    import pyodbc

    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    cursor.execute(sql)

    return cursor