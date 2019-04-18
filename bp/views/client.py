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
    result = ""
    if request.method == 'POST':
        form = ClientForm(request.POST)

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
            
            ## API CALL ##

            url = "https://ussouthcentral.services.azureml.net/workspaces/c3b894622cb140d7ae95ad0b2b167122/services/981c9c29bb0e4184b7f379339127844d/execute"

            querystring = {"api-version":"2.0","details":"true"}

            payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"LeadSource\",\r\n        \"RepliesFromClient\",\r\n        \"EmailsToClient\",\r\n        \"TotalTickets\",\r\n        \"DaysAsClient\",\r\n        \"Num_Locations\",\r\n        \"FB\",\r\n        \"PE_Videos\",\r\n        \"SEONumeric\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"Call Floor\",\r\n          \"500\",\r\n          \"600\",\r\n          \"800\",\r\n          \"2800\",\r\n          \"2\",\r\n          \"1\",\r\n          \"1\",\r\n          \"2\"\r\n        ]\r\n      ]\r\n    }\r\n  },\r\n  \"GlobalParameters\": {}\r\n}"
            headers = {
                'Authorization': "Bearer AbnjLEx45qpNmNSIEnSeIlEIMbn07O70Rl9MTchYD3uhLp9YEww/Z87E8nVroUkJ05qtj/6EHs6OSnbAGj9k7w==",
                'Content-Type': "application/json",
                'cache-control': "no-cache",
                'Postman-Token': "bf48bd01-9c80-4679-97bc-c8b86b7369c2"
                }

            response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
            
            data = response.json()
            result = data["Results"]["output1"]["value"]["Values"][0][0]
            
    else:
        form = ClientForm()
    
    context = {
        'form': form,
        'result': result,
    }

    return request.dmp.render('client.html', context)

class ClientForm(forms.Form):    
    
    LEAD_CHOICES = (
        ('Upgrade', 'Upgrade'), 
        ('Referral', 'Referral'), 
        ('Call Floor', 'Call Floor'), 
        ('Default Team', 'Default Team'), 
        ('Other', 'Other'), 
        ('not tracked', 'Not Tracked'),
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



