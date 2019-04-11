# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555012760.4931989
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/Intex/account/templates/delete.html'
_template_uri = 'delete.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        doctor = context.get('doctor', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        doctor = context.get('doctor', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <table class="prescribers">\r\n        <tr>\r\n            <th><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/user.png" alt="user"></th>\r\n            <th>Name</th>\r\n            <th>Gender</th>\r\n            <th>Credentials</th>\r\n            <th>State</th>\r\n            <th>Specialty</th>\r\n        <tr>\r\n        <tr>\r\n            <td><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/user.png" alt="user"></td>\r\n            <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctor[0]))
        __M_writer('</td>\r\n            <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctor[1]))
        __M_writer('</td>\r\n            <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctor[2]))
        __M_writer('</td>\r\n            <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctor[3]))
        __M_writer('</td>\r\n            <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctor[4]))
        __M_writer('</td>\r\n        </tr>\r\n    </table>\r\n    <form action="/account/confirm_delete/" method="POST">\r\n        <input type="hidden" name="doctorID" value="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctor[5]))
        __M_writer('"/>\r\n        <button type="submit" class="page-btn">Confirm Delete?</button>\r\n    </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/stick/Developer/Intex/account/templates/delete.html", "uri": "delete.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "49": 3, "58": 3, "59": 6, "60": 6, "61": 14, "62": 14, "63": 15, "64": 15, "65": 16, "66": 16, "67": 17, "68": 17, "69": 18, "70": 18, "71": 19, "72": 19, "73": 23, "74": 23, "80": 74}}
__M_END_METADATA
"""
