from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django import forms
from django.core.exceptions import ValidationError

@view_function
def process_request(request):
    request.session.flush() 
    if request.method == 'POST':
        form = ClientForm(request.POST)

        if form.is_valid():
            user = authenticate(request, username=form["username"].value(), password=form["password"].value())
            login(request, user)
            return HttpResponseRedirect('/bp/index/')
        else:
            pass
    else:
        form = ClientForm()
    
    context = {
        'form': form,
    }

    return request.dmp.render('client.html', context)

class ClientForm(forms.Form):    
    
    CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)

    LeadSource = forms.ChoiceField(
                label="Lead Source",
                choices=CHOICES,
                widget=forms.Select(attrs={'class': 'req'})
                )
    RepliesFromClient = forms.IntegerField(
                label="Replies From Client",
                initial=0,
                min_value=0,
                widget=forms.NumberInput(attrs={'class': 'req'})
                )
    EmailsToClient = forms.IntegerField(
                label="Replies From Client",
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
                choices=(("1", "Yes"), ("0", "No"),),
                widget=forms.Select(attrs={'class': 'req'})
                )
    PE_Videos = forms.ChoiceField(
                choices=(("1", "Yes"), ("0", "No"),),
                widget=forms.Select(attrs={'class': 'req'})                
                )
    
    # SEONumeric

