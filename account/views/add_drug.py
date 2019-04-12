from django.conf import settings
from django_mako_plus import view_function, jscontext
import pyodbc
from django.http import HttpResponseRedirect
from django.forms import forms

@view_function
def process_request(request,  docID:int=0):
    if not request.user.has_perm('account.change_user'):
        return HttpResponseRedirect('/account/permission_denied/') 

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
    
    sql = '''SELECT IsOpioid FROM Opioids WHERE DrugName = ? '''
    result = runSQL(sql, (drug))

    for drugs in result:
        opioid = drugs[0]

    if opioid == 1: 
        sql = ('''UPDATE prescriber
            SET Opioid_Prescriber = 1 
            WHERE DoctorID = ? ; 
            
            UPDATE prescriber 
            SET 
                TotalOpioidPerscription = TotalOpioidPerscription + ?
            WHERE
                DoctorID = ?
            ''')
        con = pyodbc.connect(settings.CONNECTION_STRING)
        cursor = con.cursor()
        cursor.execute(sql, (docID, qty, docID))
        cursor.commit()


    sql = ('''UPDATE triple  
            SET Qty = Qty + ? 
            WHERE DoctorID = ? 
            AND Drug = ? 
        IF @@ROWCOUNT=0
            INSERT INTO triple (Qty, DoctorID, Drug) 
            VALUES (?, ?, ?);''')

    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    cursor.execute(sql, (qty, docID, drug, qty, docID, drug))
    cursor.commit()

    columnDrug = drug.replace(".", "_")
    
    sql = ('''UPDATE prescriber 
            SET 
                TotalPrescriptions = TotalPrescriptions + ?
            WHERE
                DoctorID = ?;
            UPDATE prescriber
            SET 
                OpioidPerscriptionRatio =  CAST(TotalOpioidPerscription/(TotalPrescriptions + .000000000000000001) as decimal (6,2))
            WHERE 
                DoctorID = ?;
            ''')
    sql += "UPDATE prescriber SET " + columnDrug + " = " + columnDrug + " + " + str(qty) + " WHERE DoctorID = " + str(docID)
    
    c = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = c.cursor()
    cursor.execute(sql, (qty, docID, docID))
    cursor.commit()