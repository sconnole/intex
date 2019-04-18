from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from decimal import Decimal
import requests

@view_function
def process_request(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/bp/login/')
    if not request.user.has_perm('account.access_bp'):
        return HttpResponseRedirect('/bp/login/')
    
    days = 0
    years = 0
    months = 0
    if request.method == 'POST':
        form = TimeForm(request.POST)

        if form.is_valid():
            lead = form["LeadSource"].value()
            replies = form["RepliesFromClient"].value()
            emails = form["EmailsToClient"].value()
            total = form["TotalTickets"].value()
            locations = form["Num_Locations"].value()
            fb = form["FB"].value()
            PatientEducation = form["PE_Videos"].value()
            status = form["StatusNumeric"].value()
            
            ## API CALL ##

            url = "https://ussouthcentral.services.azureml.net/workspaces/a6a8851e6a794d0ab9b2221bf735138c/services/94fcbd2942024dfeaeec95aa5073e9fe/execute"

            querystring = {"api-version":"2.0","details":"true"}

            payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"RepliesFromClient\",\r\n        \"EmailsToClient\",\r\n        \"TotalTickets\",\r\n        \"LeadSourceNumeric\",\r\n        \"Num_Locations\",\r\n        \"FB\",\r\n        \"PE_Videos\",\r\n        \"StatusNumeric\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"" + replies + "\",\r\n          \"" + emails + "\",\r\n          \"" + total + "\",\r\n          \"" + lead + "\",\r\n          \"" + locations + "\",\r\n          \"" + fb + "\",\r\n          \"" + PatientEducation + "\",\r\n          \"" + status + "\"\r\n        ]\r\n      ]\r\n    }\r\n  },\r\n  \"GlobalParameters\": {}\r\n}"
            headers = {
                'Authorization': "Bearer d8BMaTmW6A3m/3HxIU5bF2W36Gv84j3bfEBymyXNxxhU0HZbt1gOSX74Kb7m/yKKIOuqoAXbuwaUnPNoUX/t9g==",
                'Content-Type': "application/json",
                'cache-control': "no-cache",
                'Postman-Token': "a59f1fcb-7dae-45cd-9904-8ba935e4747a"
                }

            response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

            data = response.json()
            result = data["Results"]["output1"]["value"]["Values"][0][0]
            days = int(round(Decimal(result), 0 ))
            years = int(days / 365)
            months = int((days % 365) * 0.0328)

    else:
        form = TimeForm()
    
    context = {
        'form': form,
        'days': days,
        'years': years,
        'months': months,
    }
   
    return request.dmp.render('time.html', context)

class TimeForm(forms.Form):    
    
    LEAD_CHOICES = (
        ('1', 'Not Tracked'),
        ('3', 'Default Team'),
        ('4', 'Call Floor'),
        ('5', 'Referral'),
        ('6', 'Upgrade'),
        ('2', 'Other'),
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
                label='Status',
                choices=(("1", "Active"), ("0", "Closed"),),
                widget=forms.Select(attrs={'class': 'req'})                
                )