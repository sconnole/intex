from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from decimal import Decimal
from django.conf import settings
import pyodbc

@view_function
def process_request(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/bp/login/')
    if not request.user.has_perm('account.access_bp'):
        return HttpResponseRedirect('/bp/login/')
    
    # success = ''
    if request.method == 'POST':
        form = DataForm(request.POST)

        if form.is_valid():
            lead = form["LeadSource"].value()
            replies = form["RepliesFromClient"].value()
            emails = form["EmailsToClient"].value()
            total = form["TotalTickets"].value()
            days = form["DaysAsClient"].value()
            locations = form["Num_Locations"].value()
            fb = form["FB"].value()
            PatientEducation = form["PE_Videos"].value()
            seo = form["SEONumeric"].value()
            status = form["StatusNumeric"].value()

            #Because the Client_ID is not an actual identity field it is not unique
            #The max value for Client_ID in the original data is 7194
            #If you ever want to reset to the original data simply run the following query:
            #       DELETE FROM Client WHERE Client_ID > 7194
            sql = ('''INSERT INTO Client (Client_ID, LeadSourceNumeric, RepliesFromClient, EmailsToClient, TotalTickets, DaysAsClient, Num_Locations, FB, PE_Videos, SEONumeric, StatusNumeric) 
                        VALUES ((SELECT MAX(Client_ID) + 1 FROM Client), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''')
            conn = pyodbc.connect(settings.BP_STRING)
            cursor = conn.cursor()
            cursor.execute(sql, (lead, replies, emails, total, days, locations, fb, PatientEducation, seo, status))
            conn.commit()

            success = 'Data Successfully Added to the Database'

    else:
        form = DataForm()
        success = 'Submit Data to be Added to the Database'
    
    context = {
        'form': form,
        'success': success,
    }
   
    return request.dmp.render('newdata.html', context)

class DataForm(forms.Form):
    
    LEAD_CHOICES = (
        ('1', 'Not Tracked'),
        ('3', 'Default Team'),
        ('4', 'Call Floor'),
        ('5', 'Referral'),
        ('6', 'Upgrade'),
        ('2', 'Other'),
        )
    
    SEO_CHOICES = (
        ("0", "None"), 
        ("1", "5 Local Key Words"), 
        ("2", "Basic"),
        ("3", "Plus"), 
        ("4", "Elite"), 
        ("5", "Custom"), 
        )

    LeadSource = forms.ChoiceField(
                label="Lead Source",
                choices=LEAD_CHOICES,
                widget=forms.Select(attrs={'class': 'req'})
                )
    RepliesFromClient = forms.IntegerField(
                label="Replies From Client",
                initial=0,
                min_value=0,
                widget=forms.NumberInput(attrs={'class': 'req'})
                )
    EmailsToClient = forms.IntegerField(
                label="Emails Sent to Client",
                initial=0,
                min_value=0,
                widget=forms.NumberInput(attrs={'class': 'req'})
                )
    TotalTickets = forms.IntegerField(
                label="Total Number of Tickets",
                initial=0,
                min_value=0,
                widget=forms.NumberInput(attrs={'class': 'req'})
                )
    DaysAsClient = forms.IntegerField(
                label="Days as a Client",
                initial=0,
                min_value=0,
                widget=forms.NumberInput(attrs={'class': 'req'})
                )
    Num_Locations = forms.IntegerField(
                label="Number of Locations",
                initial=0,
                min_value=0,
                widget=forms.NumberInput(attrs={'class': 'req'})
                )
    FB = forms.ChoiceField(
                label='Facebook',
                choices=(("1", "Yes"), ("0", "No"),),
                widget=forms.Select(attrs={'class': 'req'})
                )
    PE_Videos = forms.ChoiceField(
                label='Patient Education Videos',
                choices=(("1", "Yes"), ("0", "No"),),
                widget=forms.Select(attrs={'class': 'req'})                
                )
    SEONumeric = forms.ChoiceField(
                label='SEO Package',
                choices=SEO_CHOICES,
                widget=forms.Select(attrs={'class': 'req'})                
                )
    StatusNumeric = forms.ChoiceField(
                label='Status',
                choices=(("1", "Active"), ("0", "Closed"),),
                widget=forms.Select(attrs={'class': 'req'})                
                )