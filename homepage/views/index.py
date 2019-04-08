from django.conf import settings
from django_mako_plus import view_function, jscontext

@view_function
def process_request(request):
    import pyodbc
    cs = (
    "DRIVER={ODBC Driver 13 for SQL Server};"
    "SERVER=tcp:eligardner.database.windows.net,1433;"
    "Datbase=INTEXII;"
    "UID=eligardner@eligardner;"
    "PWD=Password413"
    )
    print(cs)

    conn = pyodbc.connect(cs)
    print("connected")
    
    cursor = conn.cursor()
    sql = "SELECT * FROM dbo.triple"

    cursor.execute(sql)

    for row in cursor:
        print(row)


    return request.dmp.render('index.html')