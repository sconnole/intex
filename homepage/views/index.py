from django.conf import settings
from django_mako_plus import view_function, jscontext
from django import forms

ROWS = 5
OFFSET = 0

@view_function
def process_request(request, page:int=0):
    OFFSET = page*ROWS
    docs = []
    drugs = []

    if request.method == 'POST': 
        form = SearchForm(request.POST)
    else: 
        form = SearchForm()

    #Maybe make this a function
    sql = ("SELECT FullName, Gender, Credentials, State, Specialty " 
            " FROM dbo.prescriber "
            " WHERE FullName LIKE '%Smith%'" 
            "   OR Credentials LIKE '%MD%'" 
            "   OR State LIKE '%UT%'"
            "   OR Specialty LIKE '%PA%'"
            " ORDER BY Lname " 
            " OFFSET " + str(OFFSET) + " ROWS"
            " FETCH NEXT " + str(ROWS) + " ROWS ONLY;")
    results = runSql(sql)
    for row in results:
        docs.append(row)
    #mkae this a function?
    sql = ("SELECT DrugName, IsOpioid "
            " FROM dbo.opioids"
            " WHERE DrugName LIKE '%phine%'"
            " ORDER BY DrugName" 
            " OFFSET " + str(OFFSET) + " ROWS"
            " FETCH NEXT " + str(ROWS) + " ROWS ONLY;")

    results = runSql(sql)
    
    for row in results: 
        drugs.append(row)

    context = {
        "prescribers": docs,
        "drugs": drugs,
        "page": page,
        "form": form
    }

    return request.dmp.render('index.html', context)
    
def runSql (sql): 
    import pyodbc

    conn = pyodbc.connect(settings.CONNECTION_STRING)
    cursor = conn.cursor()
    cursor.execute(sql)

    return cursor

class SearchForm(forms.Form):
    search = forms.CharField(label=u'',
        widget=forms.TextInput(attrs={'placeholder': 'Search...', 'id':'mySearch'}))

        