from django.conf import settings
from django_mako_plus import view_function, jscontext
import pyodbc
from django.http import HttpResponseRedirect
from django.forms import forms

@view_function
def process_request(request, docID:int=0):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')
    if not request.user.has_perm('account.change_user'):
        return HttpResponseRedirect('/account/permission_denied/') 
    print(request.method)
    print(docID)
    if request.method == "POST":
        drug = request.POST['drug']
        qty = request.POST['quantity']
        updateDB(drug, qty, docID)
        return HttpResponseRedirect("/account/add_drug/{}".format(docID))

    sql = ('''SELECT FullName  
            FROM dbo.prescriber 
            WHERE DoctorID = ?
           ''')

    docs = runSQL(sql, (docID))
    for item in docs:
        doctor = item
    
    sql = "SELECT DrugName FROM Opioids"          
    dropdown = SQL(sql)

    sql = ('''SELECT Drug, Qty
            FROM Triple 
            WHERE DoctorID = ? ''')

    current_drugs = runSQL(sql, (docID)) 
    

    context = {
        "doctor": doctor,
        "dropdown": dropdown,
        "current_drugs": current_drugs,
        "doctorID": docID
    }

    return request.dmp.render('add_drug.html', context)

def SQL (sql):
    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    return cursor.execute(sql)

def runSQL (sql, param):
    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    return cursor.execute(sql, (param))

def updateDB(drug, qty, docID):
    
    print("UPDATE------------------")
    sql = '''SELECT IsOpioid FROM Opioids WHERE DrugName = ? '''
    result = runSQL(sql, (drug))

    for drug in result:
        Opioid = drug
    print(Opioid)

    sql = ('''UPDATE triple 
            SET Qty = Qty + ? 
            WHERE DoctorID = ? 
            AND Drug = ?
        IF @@ROWCOUNT=0
            INSERT INTO
            triple (DoctorID, Drug, Qty) 
            values(?, ?, ?);
            ''')
    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    #cursor.execute(sql, (qty, docID, drug, docID, drug, qty))
    
    return