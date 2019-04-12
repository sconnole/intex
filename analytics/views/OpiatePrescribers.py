from django.conf import settings
from django_mako_plus import view_function, jscontext
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')
    if not request.user.has_perm('account.view_analytics'):
        return HttpResponseRedirect('/account/permission_denied/')
    return request.dmp.render('opiateprescribers.html')