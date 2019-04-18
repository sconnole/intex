from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
import requests

@view_function
def process_request(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/bp/login/')
    
    if request.method == 'POST':
        form = TimeForm(request.POST)

        if form.is_valid():
            lead = form["LeadSource"].value()
            replies = form["RepliesFromClient"].value()
            emails = form["EmailsToClient"].value()
            total = form["TotalTickets"].value()
            days = form["DaysAsClient"].value()
            locations = form["Num_Locations"].value()
            fb = form["FB"].value()
            PatientEducation = form["PE_Videos"].value()
            status = form["StatusNumeric"].value()
            
            ## API CALL ##

            url = "https://ussouthcentral.services.azureml.net/workspaces/a6a8851e6a794d0ab9b2221bf735138c/services/94fcbd2942024dfeaeec95aa5073e9fe/execute"

            querystring = {"api-version":"2.0","details":"true"}

            payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"DaysAsClient\",\r\n        \"LeadSourceNumeric\",\r\n        \"Num_Locations\",\r\n        \"FB\",\r\n        \"PE_Videos\",\r\n        \"StatusNumeric\",\r\n        \"LnPlus1(RepliesFromClient)\",\r\n        \"LnPlus1(EmailsToClient)\",\r\n        \"LnPlus1(TotalTickets)\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"0\",\r\n          \"0\",\r\n          \"0\",\r\n          \"0\",\r\n          \"0\",\r\n          \"0\",\r\n          \"0\",\r\n          \"0\",\r\n          \"0\"\r\n        ]\r\n      ]\r\n    }\r\n  },\r\n  \"GlobalParameters\": {}\r\n}"
            headers = {
                'Authorization': "Bearer d8BMaTmW6A3m/3HxIU5bF2W36Gv84j3bfEBymyXNxxhU0HZbt1gOSX74Kb7m/yKKIOuqoAXbuwaUnPNoUX/t9g==",
                'Content-Type': "application/json",
                'cache-control': "no-cache",
                'Postman-Token': "9c3deea1-5752-457c-9d66-7f5708c5bb35"
            }

            response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

            print(response.text)
            
    else:
        form = TimeForm()
    
    context = {
        'form': form,
    }
   
    return request.dmp.render('time.html', context)

class TimeForm(forms.Form):    
    
    LEAD_CHOICES = (
        ('1', 'Not Tracked'),
        ('2', 'Default Team'),
        ('3', 'Call Floor'),
        ('4', 'Referral'),
        ('5', 'Upgrade'),
        ('6', 'Other'),
        ('0', 'Blank'),
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
    StatusNumeric = forms.ChoiceField(
                choices=(("1", "Yes"), ("0", "No"),),
                widget=forms.Select(attrs={'class': 'req'})                
                )