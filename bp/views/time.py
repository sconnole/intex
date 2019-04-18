from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/bp/login/')
    
    if request.method == 'POST':
        form = TimeForm(request.POST)

        if form.is_valid():
            lead = form["LeadSource"]
            print("|||||||||||||||||", lead)
            return HttpResponseRedirect('/bp/index/')
        else:
            pass
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