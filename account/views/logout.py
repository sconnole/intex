from django.contrib.auth import logout
from django_mako_plus import view_function
from django.http import HttpResponse, HttpResponseRedirect

@view_function
def process_request(request):
    logout(request)
    return HttpResponseRedirect('/account/login')   