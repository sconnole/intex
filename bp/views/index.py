from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/bp/login/')
    if not request.user.has_perm('account.access_bp'):
        return HttpResponseRedirect('/bp/logout/')

    context = {
        
    }
   
    return request.dmp.render('index.html', context)