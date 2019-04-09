# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554837957.65242
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/Intex/account/views/login.py'
_template_uri = '/account/views/login.py'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('from django.conf import settings\r\nfrom django_mako_plus import view_function\r\nfrom django import forms\r\nfrom django.core.exceptions import ValidationError\r\nfrom django.contrib.auth import authenticate, login\r\nfrom account.models import User\r\nfrom django.http import HttpResponse, HttpResponseRedirect\r\n\r\n@view_function\r\ndef process_request(request):\r\n    \r\n    if request.method == \'POST\':\r\n        # Create a form instance and populate it with data from the request (binding):\r\n        form = LoginForm(request.POST)\r\n\r\n        if form.is_valid():\r\n            user = authenticate(request, username=form["username"].value(), password=form["password"].value())\r\n            login(request, user)\r\n            return HttpResponseRedirect(\'/homepage/index/\')\r\n        else:\r\n            pass\r\n\r\n    else:\r\n        form = LoginForm()\r\n\r\n    context = {\r\n        \'form\': form,\r\n    }\r\n    return request.dmp.render(\'/account/templates/login.html\', context)\r\n\r\nclass LoginForm(forms.Form):\r\n    username = forms.CharField(label=u\'Username\', max_length=30)\r\n    password = forms.CharField(\r\n                                label=u\'Password\',\r\n                                widget=forms.PasswordInput()\r\n                                )\r\n    def clean(self):\r\n        data = self.cleaned_data\r\n        user = authenticate(username=data.get("username"), password=data.get("password"))\r\n        if user is None:\r\n            raise ValidationError(\'Invalid username or password.\')\r\n        return data')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/stick/Developer/Intex/account/views/login.py", "uri": "/account/views/login.py", "source_encoding": "utf-8", "line_map": {"18": 0, "23": 1, "29": 23}}
__M_END_METADATA
"""
