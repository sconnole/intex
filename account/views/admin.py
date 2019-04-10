from django.conf import settings
from django_mako_plus import view_function
from homepage.views.index import SearchForm
from django.http import HttpResponseRedirect

ROWS = 5
OFFSET = 0

@view_function
def process_request(request):
    if not request.user.has_perm('account.add_user'):
        return HttpResponseRedirect('/account/permission_denied/') 

    

    context = {
        "form": SearchForm()
    }

    return request.dmp.render('/account/templates/admin.html', context)
